
class Employee:
  """Employee description"""

  def __init__(self, name="unknown employee", title="job unknown", start_date="start date unknown"):
    self.name = name
    self.title = title
    self.start_date = start_date

  def __str__(self):
    return f"{self.name}"
  def job_title(self):
    return f"{self.title}"
  def employee_start_date(self):
    return f"{self.start_date}"
  def employee_data(self):
    return f"{self.name}, {self.title}, {self.start_date}"

employee = Employee('Robby')
print(employee)

employee_profile = Employee(name='Robby', start_date='12_aug_08')
print(employee_profile.employee_data())

employee_title = Employee(title='Dev')
print(employee_title.job_title())

# ----

class Company(object):
  """This represents a company in which people work"""

  def __init__(self, company_name='company', date_founded='date founded'):
      self.company_name = company_name
      self.date_founded = date_founded
      self._employees = list()

  def get_company_name(self):
    """Returns the name of the company"""
    return self.company_name

  def get_date_founded(self):
    """Returns the date company was founded"""
    return self.date_founded

  @property
  def employees(self):
    companies_and_emps = dict()
    company = self.get_company_name()
    for emp in self._employees:
      try:
        companies_and_emps[company].append(emp.name)
      except KeyError:
        companies_and_emps[company] = list()
        companies_and_emps[company].append(emp._employee_name)

  @employees.setter
  def employees(self, emp):
    self._employees.append(emp)

  def __str__(self):
    return f"{self.company_name}"

# ------
 



  