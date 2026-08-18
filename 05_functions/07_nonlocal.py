def update_order():
    chai_type = "Elaichi"
    print("Before kitchen update", chai_type)
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()