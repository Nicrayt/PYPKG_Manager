def userconfirmation(message):
    """Return True if input == y"""
    # Ask the user for confirmation and return True only if the answer is "y"
    try:
        return input(f"{message} (Y/n): ").strip().lower() in ("", "y", "yes")
    except KeyboardInterrupt: return
    except Exception as error: print(f"An unexpected error occurred : {error}"); return