#!/usr/bin/python

import billObj
import sys
import os



if __name__ == "__main__":

    bill = billObj.bill(4)
    bill.debug_add_example_item()
    bill.print_bill()

    print "\n"

    bill.update_info()
    bill.print_info()

    print "\n"

    #bill.divvy_bill_simple()

    bill.divvy_bill_adv()