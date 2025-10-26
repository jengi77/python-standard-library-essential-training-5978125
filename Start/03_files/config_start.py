# read the contents of configuration files
import configparser


# TODO: Create the configuration parser
parser = configparser.ConfigParser()

# TODO: Read the configuration file
parser.read("config.cfg")

# TODO: print the sections
print(parser.sections())
print(parser.has_section("Section 1"))
print(parser.has_section("Section 7"))

# TODO: Access one of the default values
print(parser['DEFAULT'][list(parser.defaults().keys())[0]])
print(parser['DEFAULT']['UseTimeTravel']) ## Wäre ein String und kein Boolean
using_time_travel = bool(parser['DEFAULT']['UseTimeTravel'])
print(using_time_travel)

# TODO: Demonstrate the getXXX convenience functions
obd = parser['DEFAULT'].getboolean('ObeyPrimeDirective')
print(obd)
print(type(obd))

speed = parser['DEFAULT'].getfloat('Ship Speed')
print(speed)

# TODO: Access a non-existent value
title = parser['DEFAULT'].getfloat('Test')
print(title)
try:
  title = parser['Section 3'].getfloat('Test')
  print(title)
except KeyError as err:
  print("Whoa! There is no ", err)  