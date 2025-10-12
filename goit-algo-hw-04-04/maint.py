from datetime import datatiem

'''
Додаток який буде зберігати нотатки
This is my note, that I am taking on my laptop
- Created on 07.10.2025 15:50 
1)створити словник та записати в ньому шнформацію
2)написати циклб який буде отримувати шнформацію від користувача та реагувати на неї

'''
note_list = []
def add_new_note(note_text, note_creation_date):
    note_creation_date= datatiem.today()
    note_list.append({'text': note_text, 'creation_date': note_creation_date})

def print_note(index: int):
    note = note_list[index]
    formated_date_creation = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f'"{note["text"]}"\n- Created on{note["creation_date"]}\n')


def print_all_notes():
    for not_index in range(len(note_list)):
        print_note(not_index)
    

text = input("Please enter your note: ")
add_new_note(text)
add_new_note(text)
add_new_note(text)
print_all_notes()
