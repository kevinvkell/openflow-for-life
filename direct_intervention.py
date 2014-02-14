# Copyright 2012 James McCauley
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This component is for use with the OpenFlow tutorial.

It acts as a simple hub, but can be modified to act like an L2
learning switch.

It's roughly similar to the one Brandon Heller did for NOX.
"""

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()



class Direct_Intervention (object):
  """
  A Tutorial object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

    # Use this table to keep track of which ethernet address is on
    # which switch port (keys are MACs, values are ports).
    self.mac_to_port = {}


  def resend_packet (self, packet_in, out_port):
    """
    Instructs the switch to resend a packet that it had sent to us.
    "packet_in" is the ofp_packet_in object the switch had sent to the
    controller due to a table-miss.
    """
    msg = of.ofp_packet_out()
    msg.data = packet_in

    # Add an action to send to the specified port
    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)

    # Send message to switch
    self.connection.send(msg)

  def act_like_switch (self, packet, packet_in):
    
    #The switch is self-learning, so store the MAC to Port of every packet passing through
    self.mac_to_port[packet.src] = packet_in.in_port

    print packet_in.in_port

    #if the packet isnt coming from the router
    if packet_in.in_port != 1:
      
      #create a new rule that says to forward it to the router first
      msg1 = of.ofp_flow_mod()
      
      #port 1 is the port in the direction of the router
      msg1.match = of.ofp_match.from_packet(packet)
      action1 = of.ofp_action_output(port = 1)
      msg1.actions.append(action1)

      #send the new rule
      self.connection.send(msg1)
      
      #send the packet
      self.resend_packet(packet_in,1)
    
      #else the packet is coming from the router
      #check if we already know the port corresponding to that mac address
    elif packet.dst in self.mac_to_port:
      
      #If so then create a rule for the table
      msg2 = of.ofp_flow_mod()
      
      #Send the packet to the correct host
      msg2.match = of.ofp_match.from_packet(packet)
      action2 = of.ofp_action_output(port = self.mac_to_port[packet.dst])
      msg2.actions.append(action2)

      #Send the new rule
      self.connection.send(msg2)

      #Send the packet
      self.resend_packet(packet_in, self.mac_to_port[packet.dst])

      #Else, it is the first time for that entry
    else:
      #Broadcast the mac address and wait for a response
      self.resend_packet(packet_in, of.OFPP_ALL)


  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.

    # Comment out the following line and uncomment the one after
    # when starting the exercise.
    self.act_like_switch(packet, packet_in)



def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Direct_Intervention(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)