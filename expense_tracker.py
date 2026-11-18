
expenses = []
def show_expenses():
    if not expenses:
        print("Aucune dépense enregistrée.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - {expense['amount']:.2f}")

def show_total():
    total = sum(item['amount'] for item in expenses)
    print(f"Total : {total:.2f}")

def add_expense():
    description = input("Description de la dépense : ")
    amount = float(input("Montant de la dépense : "))
    expenses.append({"description": description, "amount": amount})

def main():
    while True:
        print("\n===== SUIVI DES DÉPENSES =====")
        print("1. Ajouter une dépense")
        print("2. Afficher les dépenses")
        print("3. Afficher le total")
        print("4. Quitter")

        choice = input("Votre choix : ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
