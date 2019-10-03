#!/usr/bin/python

# ----------------- #
#      IMPORTS      #
# ----------------- #
import sys

class contributor():

	base_total = 0.00
	tax = 0.00
	tip = 0.00

	def __init__(self, name, tax_rate, tip_percentage):
		self.name = name
		self.tax_rate = tax_rate
		self.tip_percentage = tip_percentage

	def set_base_total(self, new_value):
		self.base_total = new_value

	def update_info(self):
		self.tax = self.base_total * (float(self.tax_rate) / 100)
		self.tip = self.base_total * (float(self.tip_percentage / 100))

	def set_name(self, new_name):
		self.name = new_name

	def print_contributor(self):
		self.update_info()
		print("Name: {}".format(self.name))
		print("Base total: {}".format(self.base_total))
		print("Tax ({}%): {}".format(self.tax_rate, self.tax))
		print("Tip ({}%): {}".format(self.tip_percentage, self.tip))
		print("Entire total: {}".format(self.base_total + self.tax + self.tip))

class bill():

	TAX_RATE = 8.75
	TIP_PERCENTAGE = 18.00
	# List of 5-tuples: name, quantity, price, quantity/price combinator, contributors
	bill = list()
	num_contributors = 0

	base_total = 0.00
	tax = 0.00
	tip = 0.00

	# Intialization
	def __init__(self, num_contributors):
		self.num_contributors = num_contributors

	# Adds an item into the 5-tuple self.bill
	def add_item(self, name="default", quantity=1, price=0.00, combinator="each", contributors=["all"]):
		# Checks
		if combinator not in ["each", "total"]:
			print("Quantity/price combinator must be either 'each' or 'total'. Defaulting to 'each'.")
		# Heretoforth (?) abbreviated to (n, q, p, qp, c)
		self.bill.append((name, quantity, price, combinator, contributors))

	def set_tax_rate(self, n):
		if self.is_num(n):
			self.TAX_RATE = float(n)
			return True
		else:
			return False

	def set_tip_percentage(self, n):
		if self.is_num(n):
			self.TIP_PERCENTAGE = float(n)
			return True
		else:
			return False

	def modify_item(self, index, item_property, new_value):
		pass

	# Gets the basic information, i.e. total, tax, tip
	def update_info(self):

		# Get total base price
		for n, q, p, qp, c in self.bill:
			self.base_total = self.base_total + (q * p) if qp is "each" else total + p

		# Get tax
		self.tax = self.base_total * (float(self.TAX_RATE) / 100)

		# Get tip based on user input percentage
		while True:
			# Python 3
			if sys.version_info >= (3, 0):
				tip_percentage = int(input("How much do you want to tip (percentage)? Default: {}%\t".format(self.TIP_PERCENTAGE)))
			# Python 2
			else:
				tip_percentage = raw_input("How much do you want to tip (percentage)? Default: {}%\t".format(self.TIP_PERCENTAGE))
			if self.is_num(tip_percentage):
				self.set_tip_percentage(tip_percentage)
				break
			elif not tip_percentage:
				break
			else:
				print("Unable to parse input. Please input a float or integer.")

		self.tip = self.base_total * (self.TIP_PERCENTAGE / 100)


	def print_info(self):
		# Print totals
		print("Base total: {}".format(self.base_total))
		print("Tax ({}%): {}".format(self.TAX_RATE, self.tax))
		print("Tip ({}%): {}".format(self.TIP_PERCENTAGE, self.tip))
		print("Entire total: {}".format(self.base_total + self.tax + self.tip))


	# Helper function checks if string is a number
	def is_num(self, n):
		try:
			float(n)
			return True
		except ValueError:
			return False

	# Divide the menu evenly between all contributors
	def divvy_bill_simple(self):
		print("Simple bill division - equal division...")
		print("Each of {} person(s) pays: ".format(self.num_contributors))
		print("Base total: {}".format(self.base_total/self.num_contributors))
		print("Tax ({}%): {}".format(self.TAX_RATE, self.tax/self.num_contributors))
		print("Tip ({}%): {}".format(self.TIP_PERCENTAGE, self.tip/self.num_contributors))
		print("Entire total: {}".format((self.base_total + self.tax + self.tip)/self.num_contributors))		

	# Divide the bill by contributors
	def divvy_bill_adv(self):

		def is_in_contributors_list(contrib_list, name):
			for index, item in enumerate(contrib_list):
				if item.name is name:
					return index
			return -1

		print("Advanced bill division - division based on contributors...")

		# Initialize individualized billing
		ans = list()
		for i in range(self.num_contributors):
			ans.append(contributor(str(i), self.TAX_RATE, self.TIP_PERCENTAGE))

		
		contrib_ctr = 0
		for index, item in enumerate(self.bill):
			n, q, p, qp, c = item
			t = q * p if qp == "each" else p
			# Divide "all" evenly
			if c == ['all']:
				for i in ans:
					i.set_base_total(i.base_total + (t / self.num_contributors))
			# Add to certain people		
			else:
				# Add new unique contributor
				t_each_contrib_add = t / len(c)
				for contrib in c:
					contrib_index = is_in_contributors_list(ans, contrib)
					# If contributor already exists
					if contrib_index >= 0:
						ans[contrib_index].set_base_total(ans[contrib_index].base_total + t_each_contrib_add)
					# Else, add new contributor
					else:
						ans[contrib_ctr].set_name(contrib)
						ans[contrib_ctr].set_base_total(ans[contrib_index].base_total + t_each_contrib_add)
						contrib_ctr = contrib_ctr + 1
		
		# debug2
		for i in ans:
			i.print_contributor()


	# Prints the bill
	def print_bill(self):
		for index, item in enumerate(self.bill):
			n, q, p, qp, c = item
			try:
				print("{}. Item: {}x {}\tPrice: {} {}\nContributors: {}".format(index + 1, q, n, p, qp, ', '.join(c)))
			except TypeError:
				self.check_menu()
				exit(1)


	# ------------- #
	#   DEBUGGING   #
	# ------------- #

	# Debugging - Add an example item
	def debug_add_example_item(self):
		self.add_item("Cheeseburger", 2, 3.99)
		self.add_item("Sundae", price=6.99, contributors=["anna","ben"])
		self.add_item("Clam Chowder", price=5.50, contributors=["charlie"])
		self.add_item("Beverage", quantity=3, price=2.99, contributors=["ben", "charlie"])

	# Debugging - goes through bill to make sure all tuple elements are of correct types and such
	def check_menu(self):
		for n, q, p, qp, c in self.bill:
			if type(n) is not str:
				print("Item name is not a string: {}".format(n))
				return False
			if type(q) is not int:
				print("Item quantity is not an integer: {}".format(q))
				return False
			if type(p) is not float:
				print("Item price is not a float: {}".format(p))
				return False
			if qp not in ["each", "total"]:
				print("Quantity/price combinator must be either 'each' or total': {}".format(qp))
				return False
			if type(c) is not list or not all(isinstance(elem, str) for elem in c):
				print("Contributors is not a list or is not a list of strings: {}".format(c))
				return False
		return True


'''
Running from MAIN

This will start up the interactive menu
'''
if __name__ == "__main__":
	# Print banner
	print("# --------- Interactive CLI operations for bill separation ---------- #")

	# Python 3x
	if sys.version_info >= (3, 0):
		num_contributors = int(input("Please input number of contributors: "))
	# Python 2
	else:
		num_contributors = raw_input("Please input number of contributors: ")

	bill = bill(num_contributors)

	