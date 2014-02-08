from mininet.topo import Topo

class Subnet_Topo(Topo):
	def __init__(self):
		Topo.__init__(self)

		# Add the host that will act as a router
		R1 = self.addHost('r1')

		# Add the rest of the hosts to the network
		H1 = self.addHost('h1')
		H2 = self.addHost('h2')
		H3 = self.addHost('h3')
		H4 = self.addHost('h4')

		# Add the switches
		S1 = self.addSwitch('s1')
		S2 = self.addSwitch('s2')

		# Add the connections between the switches and routers
		self.addLink(R1, S1)
		self.addLink(R1, S2)
		self.addLink(S1, S2)

		# Connect the hosts to the network
		self.addLink(H1, S1)
		self.addLink(H2, S1)
		self.addLink(H3, S2)
		self.addLink(H4, S2)

		# addLink (unit1, unit2, bw=10, delay='5ms', max_queue_size=1000, loss=10, use_htb=True)
		# bw(BandWidth) in Mb/s, dalay can be ms/us/s/etc., loss is a percentage out of 100

topos = {
	'subnet': (lambda: Subnet_Topo())
}


