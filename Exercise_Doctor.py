from queue import Queue

patient_queue = Queue()

while True:
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter patient name: ")
        patient_queue.put(name)
        print(f"Patient '{name}' registered.")

    elif choice == '2':
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            remove_patient = input("enter the patient name: ")
            patient_queue.get(remove_patient)
            print(f"Patient {remove_patient} removed after meeting the doctor.")
            
    elif choice == '3':
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            print("Current patient queue:")
            for i, patient in enumerate(patient_queue.queue, start=1):
                print(f"{i}. {patient}")
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")