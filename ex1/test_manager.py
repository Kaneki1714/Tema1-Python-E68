from employee import Employee
from manager import Manager


def test_creare_manager():
    """Verifica atributele unui Manager si cresterea contoarelor."""
    emp_initial = Employee.empCount
    mgr_initial = Manager.mgr_count

    mgr = Manager(
        "Valeanu Stefan-Marian",
        9500,
        {"Review cod proiect": "In progress"},
        "Team Lead",
        "E68_Valeanu_Constantin"
    )

    assert mgr.name == "Valeanu Stefan-Marian"
    assert mgr.salary == 9500
    assert mgr.position == "Team Lead"
    assert mgr.department == "E68_Valeanu_Constantin"
    assert Employee.empCount == emp_initial + 1
    assert Manager.mgr_count == mgr_initial + 1


def test_afisare_doar_nume(capsys):
    """Verifica cerinta X%6 == 1: display_employee afiseaza doar numele."""
    mgr = Manager(
        "Valeanu Stefan-Marian",
        9500,
        {"Review cod proiect": "In progress"},
        "Team Lead",
        "E68_Valeanu_Constantin"
    )

    mgr.display_employee()
    rezultat = capsys.readouterr().out

    assert "Valeanu Stefan-Marian" in rezultat
    assert "9500" not in rezultat
