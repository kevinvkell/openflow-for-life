from mininet.topo import Topo

class Direct_Topo(Topo):
	def __init__(self):
		Topo.__init__(self)

		# Add the host that will act as a router
		R1 = self.addHost('r1')

		# Add the host that will act as an IDS
		IDS = self.addHost('ids')

		# Add the rest of the hosts to the network
		H1 = self.addHost('h1')
		H2 = self.addHost('h2')
		H3 = self.addHost('h3')
		H4 = self.addHost('h4')

		# Add the switches
		S1 = self.addSwitch('s1')

		# Add the connections between the ids and the switch
		self.addLink(IDS, S1)

		# Connect the hosts to the network
		self.addLink(H1, S1)
		self.addLink(H2, S1)
		self.addLink(H3, S1)
		self.addLink(H4, S1)

		# Connect the router to the ids
		self.addLink(R1, IDS)

class Indirect_Topo(Topo):
	def __init__(self):
		Topo.__init__(self)

		# Add the host that will act as a router
		R1 = self.addHost('r1')

		# Add the host that will act as an IDS
		IDS = self.addHost('ids')

		# Add the rest of the hosts to the network
		H1 = self.addHost('h1')
		H2 = self.addHost('h2')
		H3 = self.addHost('h3')
		H4 = self.addHost('h4')

		# Add the switches
		S1 = self.addSwitch('s1')

		# Connect the router and ids to the switch
		self.addLink(R1, S1)
		self.addLink(IDS, S1)

		# Connect the hosts to the network
		self.addLink(H1, S1)
		self.addLink(H2, S1)
		self.addLink(H3, S1)
		self.addLink(H4, S1)

topos = {
	'direct' : (lambda: Direct_Topo()),
	'indirect': (lambda: Indirect_Topo())
}
