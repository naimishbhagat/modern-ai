def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai....")
        if flavor == "unknown":
            raise ValueError("We dont know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is serving")
    finally:
        print("Next customer please")

serve_chai("masala")
serve_chai("unknown")