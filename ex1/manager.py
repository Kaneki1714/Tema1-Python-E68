from employee import Employee


class Manager(Employee):
    """Clasa derivata din Employee pentru gestionarea managerilor."""
    mgr_count = 0

    def __init__(self, name, salary, task, position, department):
        Employee.__init__(self, name, salary)

        if isinstance(task, dict):
            self.tasks = task
        else:
            self.tasks = {task: "New"}

        self.position = position
        self.department = department
        Manager.mgr_count += 1

    def display_employee(self):
        """Suprascriere pentru X % 6 == 1 (13 % 6 == 1): afiseaza doar numele angajatului."""
        print(self.name)

    def __del__(self):
        Manager.mgr_count -= 1
        Employee.__del__(self)


if __name__ == "__main__":
    emp1 = Employee("Onita Taric", 5000)
    emp2 = Employee("Georgescu Ian", 5800)

    mgr1 = Manager(
        name="Valeanu Stefan-Marian",
        salary=9500,
        task={"Review cod proiect": "In progress"},
        position="Team Lead",
        department="E68_Valeanu_Constantin"
    )

    print("Obiecte Manager (X%6 == 1 -> doar numele)")
    mgr1.display_employee()

    print("\nObiecte Employee")
    emp1.display_employee()
    emp2.display_employee()

    print("\nValoarea atributului emp_count")
    print(f"emp_count pentru instanta Employee (emp1): {emp1.empCount}")
    print(f"emp_count pentru instanta Manager (mgr1): {mgr1.empCount}")
    print(f"mgr_count pentru clasa Manager: {Manager.mgr_count}")
