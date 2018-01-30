import random
import unittest

class tree_obj(object):
	class node_obj(object):
		def __init__(self, data):
			self.data = data
			self.left = None
			self.right = None
			return
	
	def __init__ (self, data):
		self.root = tree_obj.node_obj(data)
		self.node_num = 1
		return
	
	def add (self, this_root, side, data):
		this_node = tree_obj.node_obj(data)
		self.node_num += 1
		if side == "L":
			this_root.left = this_node
		elif side == "R":
			this_root.right = this_node
		return
	
	def get_random_node(self):
		"""
		when called must return a random node from the tree
		brute force approach: copy all nodes to a linked list and then move down the list a random number of steps
		approach: perform an in order traversal for random number of steps
		"""
		steps_to_take = int((self.node_num + 1) * random.random())
		if steps_to_take == 0:
			return self.root
		this_node = self.root
		stack = []
		steps_taken = 0
		while True:
			while this_node != None:
				stack.append(this_node)
				this_node = this_node.left
			this_node = stack.pop()
			steps_taken += 1
			if steps_taken == steps_to_take:
				return this_node
			while( (this_node.right != None) and (len(stack) != 0) ):
				this_node = stack.pop()
				steps_taken += 1
				if steps_taken == steps_to_take:
					return this_node
			this_node = this_node.right
		return

class TestTree(unittest.TestCase):
	def test_init(self):
		this_tree = tree_obj(20)
		self.assertEqual( this_tree.root.data, 20)
	def test_add(self):
		this_tree = tree_obj(20)
		this_tree.add(this_tree.root, "L", 10)
		self.assertEqual( this_tree.root.left.data, 10)
	def test_get_random_node(self):
		this_tree = tree_obj(20)
		this_tree.add(this_tree.root, "L", 10)
		this_tree.add(this_tree.root, "R", 30)
		this_tree.add(this_tree.root.right, "L", 25)
		this_tree.add(this_tree.root.right, "R", 35)
		self.assertTrue( this_tree.get_random_node().data in [10, 20, 25, 30, 35] )
unittest.main()