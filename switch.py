"""! @brief Handle switch statement gracefully. """

##
# @file      switch.py
# @author    Mohammad Huwaidi
# @copyright SECA4
# @date      2022/07/24
# @package   Switch
# @version   1.0.0
# @brief     An alternative to switch statement.
# @details   Handle switch statement gracefully.
#

# FILL-OUT: (please fill out the following): 
__file__      = "switch.py"
__program__   = "N/A"
__whoami__    = "Switch"
__version__   = "1.0.0"
__author__    = "Mohammad Huwaidi"
__email__     = "huwaidi@seca4.com"
__website__   = 'http://www.seca4.com'
__group__     = "HPC Support"
__copyright__ = "Copyright(c) 2022 SECA4"
__license__   = "N/A"
__date__      = "$Date: 2022/07/25 15:31:00"
__update__01  = "<date_stamp>"  # Add each update separately with a date stamp.

""" NOTE
    If you believe that you can enhance (debug) the code, please be our guest.
    Please, deliver your modifications and suggestions to us.
"""

import sys


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
#  @brief   Return the class name.
#  @return  The class name of this file.
#  @details Each file has a unique name stored in variable \__whoami__ that is
#           the programmer's responsibility to provide.
#
def whoami() -> str:
  """
  Return the name of the main class in this file. Note that such a function
  is pertinent to this file. The same function name in a different file
  (package) produces a different identity.
  """
  return __whoami__


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
#  @brief   Print to standard error.
#  @param   [in] msg  The message to be printed.
#  @return  NA.
#  @details Usually, the standard error is printed in red to alarm the user.
#
def print_error(msg):
  """Print a message to the standard error"""
  print(msg, file=sys.stderr)


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
# @brief   A function that does nothing.
# @return  NA.
# @details A dummy function to satisfy some condition to avoid
#          raising an exception.
#
def none(*args, **kwargs): pass


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
# @brief   Used for testing purposes.
# @return  NA. However, the user can return anything she wishes to.
# @details A function to call for testing purposes. The user may modify this
#          function as she wishes.
#
def default_function(*args, **kwargs):
  print('Calling the default function.')
  pass


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
# @brief   Raise an exception when a case is missing.
# @return  NA.
# @details The user does not have to raise an exception. But this function is
#          available whenever the user does not want to handle missing cases.
#          Please, note that this is not the default function to call when
#          missing a case. The user may override handling missing cases. This is
#          just a bonus addition to handle both 'default' behavior and when a
#          case is missing to enforce some coding practices.
#
def raise_exception(*args, **kwargs):
  exception = "Encountered a case that cannot deal with"
  msg       = None

  if 'msg'       in kwargs: msg       = kwargs['msg']
  if 'exception' in kwargs: exception = kwargs['exception']

  if msg: print_error(msg)

  raise Exception(exception)


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
# @brief   Handle a missing case
# @return  NA.
# @details Handle a missing case. The user may assign it to a different
#          function that does not need to raise an exception.
#
def missing_case(*args, **kwargs):
  raise_exception(msg="Encountered a missing case that cannot deal with!")


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
# @brief   Provide a class alternative to the switch statement.
# @return  An object of class Switch.
# @details The switch (match) statement has been added lately to Python. Python
#          is a dynamic language with more graceful alternatives that cost only
#          O(1) instead of O(N), where N is the number of cases within a given
#          switch statement.
#          <br>
#          We need to understand that this class handles a default case that is
#          different from a missing case. The user may have them act similarly
#          or differently. This gives more options to the user. A default case
#          is a case name 'default' and stored in the dictionary of viable
#          cases. A missing function is not available and not viable. The user
#          may handle each as she wishes. The default for handling a missing
#          case is to act normally as hitting a 'default' case. Nevertheless,
#          the user may want to restrict certain coding practices, or perform
#          some testing.
#
class Switch:
  """ The switch statement has been added lately to Python. Python is a
      dynamic language with more graceful alternatives that cost only O(1)
      instead of O(N), where N is the number of cases within a given switch
      statement.
  """

  ## Doxygen documentation
  #  @brief   A Switch object instantiation.
  #  @param   [in] self  A reference to the current object.
  #  @param   [in] dflt  The default function to call when there is no match.
  #  @param   [in] miss  Handle a missing case.
  #  @return  An object of the Switch class.
  #  @details Instantiate a Switch object.
  #
  def __init__(self,  # Object reference.
               dflt=None,  # Default function to call by default.
               miss=None,  # Handle a missing case.
               ):

    """
    Initialize an object of Switch class.
    INPUT
      self: A reference of the object itself.
      dflt: The default function to call when default is specified.
      miss: The default function to call when there is no match.
    OUTPUT
      N/A.
    RETURN
      An object of the Switch class.
    """

    if not dflt: dflt = self.default_function
    if not miss: miss = self.default_function

    self.__default = dflt
    self.__cases = {}
    self.__missing_case = miss
    self.__cases['default'] = self.__default

  ## Doxygen documentation
  #  @brief   Get a dictionary of all cases.
  #  @param   [in] self  A reference to the current object.
  #  @return  A dictionary of all the viable cases.
  #  @details Get a dictionary of all viable cases.
  #
  def get_all_cases(self):
    return self.__cases

  ## Doxygen documentation
  #  @brief   Merge a dictionary into an existing Switch set.
  #  @param   [in] self   A reference to the current object.
  #  @param   [in] cases  Cases to add to the Switch set.
  #  @return  A new dictionary with the newly added set.
  #  @details Merge an existing dictionary of case-function pair. PLEASE, note
  #           that existing cases will be overridden if a collision happens.
  #           This is provided for convenience if the user wishes to copy from
  #           an existing set.
  #
  def merge(self, cases: dict) -> dict:
    for key, val in cases.items():
      self.update(key, val)

    return self.get_all_cases()

  ## Doxygen documentation
  #  @brief   Get a case function of the switch statement.
  #  @param   [in] self    A reference to the current object.
  #  @param   [in] a_case  A case to reference in the switch cases.
  #  @return  A case if included within the set of switch cases; otherwise,
  #           the default for a missing function.
  #  @details Get an item within a dictionary of cases.
  #
  def __getitem__(self, a_case, *args, **kwargs):
    the_case = self.__missing_case
    if a_case in self.__cases:
      the_case = self.__cases[a_case]

    return the_case

  ## Doxygen documentation
  #  @brief   Update a case of the switch statement.
  #  @param   [in] self        A reference to the current object.
  #  @param   [in] a_case      A case to add to the switch cases.
  #  @param   [in] a_function  A function associated with a given case.
  #  @return  NA.
  #  @details If the case is new, create a new entry; otherwise; update.
  #
  def __setitem__(self, a_case, a_function):
    self.update(a_case, a_function)

  ## Doxygen documentation
  #  @brief   Check if a case is included in the switch set.
  #  @param   [in] self    A reference to the current object.
  #  @param   [in] a_case  A case to check that it is in the switch cases.
  #  @return  True if the case is within the cases set; otherwise, False.
  #  @details Check if a given case is handled or not.
  #  @sa      run
  #
  def __contains__(self, a_case):
    return a_case in self.__cases

  ## Doxygen documentation
  #  @brief   Return the switch set size.
  #  @param   [in] self  A reference to the current object.
  #  @return  The number of elements in cases to handle.
  #  @details Return the length of the set size including the default case.
  #           This function will return at least 1 to cover the default case.
  #           The missing case is not handled.
  #
  def __len__(self):
    return len(self.__cases)

  ## Doxygen documentation
  #  @brief   Delete a case.
  #  @param   [in] self    A reference to the current object.
  #  @param   [in] a_case  A case to delete from the switch cases.
  #  @param   [in] args    A list of nameless arguments.
  #  @param   [in] kwargs  A dictionary of named arguments.
  #  @return  NA.
  #  @details Delete a case from the switch set. This function is idempotent.
  #
  def __delitem__(self, a_case, *args, **kwargs):
    if a_case in self.__cases:
      del self.__cases[a_case]

  ## Doxygen documentation
  #  @brief   Update a case of the switch statement.
  #  @param   [in] self         A reference to the current object.
  #  @param   [in] a_case       A case to add/update.
  #  @param   [in] a_functions  A function to associate with the given case.
  #  @return  NA.
  #  @details If the case is new, create a new entry; otherwise; update.
  #           The user may update any case, including the 'default' one.
  # 
  def update(self, a_case, a_function):
    if a_case in self.__cases:
      print_error('Switch.update: ' + str(a_case) +
                  ' already exists and will be overridden.')

    self.__cases[a_case] = a_function

  # 0000000011111111112222222222333333333344444444445555555555666666666677777777778
  # 2345678901234567890123456789012345678901234567890123456789012345678901234567890
  ##
  # @brief   The default function for a case.
  # @return  None. The user can return anything she wishes to.
  # @details A default function to call.
  #
  def default_function(self, *args, **kwargs):
    return none

  ## Doxygen documentation
  #  @brief   Run a function for a given case.
  #  @param   [in] self    A reference to the current object.
  #  @param   [in] a_case  The case of the switch.
  #  @param   [in] args    A list of nameless arguments.
  #  @param   [in] kwargs  A dictionary of named arguments.
  #  @return  The result of the function being invoked.
  #  @details Another method provided to run a function.
  #  @sa      \__setitem__
  #   
  def run(self, a_case, *args, **kwargs):
    the_case = self.__missing_case
    if a_case in self.__cases:
      the_case = self.__cases[a_case]

    return the_case(*args, **kwargs)

  ## Doxygen documentation
  #  @brief   Formatting the information the user can see.
  #  @param   [in] self A reference to the current object.
  #  @return  A formatted string (i.e., each case on a separate line).
  #  @details Format the information of the object (usually used by the print
  #           function).
  #       
  def __str__(self):
    """Prepare a printable version of the object information."""

    l = []
    for key in sorted(self.__cases.keys()):
      l.append(key + " = " + str(self.__cases[key]))

    l.append("<missing> = " + str(self.__missing_case))

    return '\n'.join(l)


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
#  @brief   Instantiate a dynamic object for this class.
#  @param   [in] args    A list of nameless arguments.
#  @param   [in] kwargs  A dictionary of named arguments.
#  @return  An object of the class defined in this scope.
#  @details This can help the programmer to acquire an instance of the class
#           without the need to know its name. This is usually safer to use.
#
def object(*args, **kwargs):
  """Return an instance of the main class defined in the current file."""
  cmd = whoami() + "(*args, **kwargs)"
  return eval(cmd)


## NOTE
# The following functions are not part of the class or its supporting functions.
# They are used only for testing purposes. Therefore, it is safe to remove them
# for production code.
##

from datetime import datetime

RUNNER_COUNT = int(10000)
LOOP_COUNT = int(10000)


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
#  @brief   A dummy function for testing purposes.
#  @param   [in] count   The count of the loop.
#  @return  NA.
#  @details To be called to test proper execution using the Switch class.
#
def runner(count: int = RUNNER_COUNT):
  sum = int(0)
  for i in range(count):
    sum += i

  return sum


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
#  @brief   A dummy function for testing purposes.
#  @param   [in] args    A list of nameless arguments.
#  @param   [in] kwargs  A dictionary of named arguments.
#  @return  NA.
#  @details To be called to test proper execution using the Switch class.
#
def foo(*args, **kwargs):
  print('Welcome to foo!')
  print(args)
  print(kwargs)


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
#  @brief   A function to test if statement.
#  @param   [in] choice     The choice that the if statement needs to select.
#  @param   [in] dummy      A dummy variable.
#  @param   [in] call_func  The function to invoke.
#  @return  NA.
#  @details Testing if statement.
#
def ifs(choice, dummy=None, call_func=whoami):
  if choice == 0:
    call_func()
  elif choice == 1:
    call_func()
  elif choice == 2:
    call_func()
  elif choice == 3:
    call_func()
  elif choice == 4:
    call_func()
  elif choice == 5:
    call_func()
  elif choice == 6:
    call_func()
  elif choice == 7:
    call_func()
  elif choice == 8:
    call_func()
  elif choice == 9:
    call_func()
  else:
    call_func()


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
#  @brief   A function to test match/case statements.
#  @param   [in] choice     The choice that the match statement needs to select.
#  @param   [in] dummy      A dummy variable.
#  @param   [in] call_func  The function to invoke.
#  @return  NA.
#  @details Testing match statement. All choices call the same function that
#           does not do anything except for returning the name of the current
#           class.
#
def cases(choice, dummy=None, call_func=whoami):
  match choice:
    case 0:
      call_func()
    case 1:
      call_func()
    case 2:
      call_func()
    case 3:
      call_func()
    case 4:
      call_func()
    case 5:
      call_func()
    case 6:
      call_func()
    case 7:
      call_func()
    case 8:
      call_func()
    case 9:
      call_func()
    case _:
      call_func()


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
#  @brief   A function to test Switch class.
#  @param   [in] choice    The choice that the Switch object needs to select.
#  @param   [in] my_cases  A Switch object.
#  @return  NA.
#  @details Testing Switch class. All choices call the same function that
#           does not do anything except for returning the name of the current
#           class.
#
def dic_switches(choice, my_cases, call_func=whoami):
  my_cases[choice]()


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
##
#  @brief   A function to time another function.
#  @param   [in] callee       The function to call
#  @param   [in] count        The number of calls to callee.
#  @param   [in] switch_case  A Switch object if required; otherwise, None.
#  @return  The time it took to call a certain function (callee) a number of
#           times (count).
#  @details Time a function.
#
def time_me(callee, count: int = LOOP_COUNT, switch_case=None,
            call_func=whoami):
  begin = datetime.now()

  for i in range(0, count):
    callee(i % 11, switch_case, call_func=call_func)

  end = datetime.now()

  return end - begin


# 0000000011111111112222222222333333333344444444445555555555666666666677777777778
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
if __name__ == "__main__":
  s1 = Switch()
  print(1, s1)
  s1.update('foo1', foo)
  print(2, s1)
  s1['foo2'] = foo
  print(3, s1)
  s1['foo1'](10, '20', hi='in', foo='foo')
  print(4, 'The length of the set is', len(s1))
  s1.run('foo2', 50, some='some')
  del s1['foo2']
  print(5, 'The length of the set is', len(s1))
  del s1['foo3']
  print(6, 'The length of the set is', len(s1))
  s1.run('nothing')
  s1['default'](None)
  s1['none'](None)
  s2 = Switch(miss=missing_case)
  s2['x'] = print
  s2.update('y', help)
  s2['x']('Hello, there!')
  s2.run('y', 'print')
  s2.run('default')
  print('default is in', 'default' in s2)
  print('nothing is in', 'nothing' in s2)
  print(s2.get_all_cases())

  # The following will raise an except; therefore, we need to capture it.
  try:
    s2['z']('nothing')
  except Exception as e:
    print_error(e)

  func = runner
  switch = Switch()
  switch.merge({0: func, 1: func, 2: func, 3: func, 4: func,
                5: func, 6: func, 7: func, 8: func, 9: func})

  print("RUNNING COUNT:", RUNNER_COUNT, "LOOP COUNT:", LOOP_COUNT)
  print("If statement     took ", time_me(ifs, call_func=func))
  print("switch statement took ", time_me(cases, call_func=func))
  print("Switch object    took ", time_me(dic_switches, switch_case=switch,
                                          call_func=func))
