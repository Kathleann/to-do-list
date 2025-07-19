import os 
os.system('cls')

# Header
print('=> To Do List <=')

task = []

# Content
try:
    while True:
        print('1. Lihat semua tugas')
        print('2. Tambah tugas')
        print('3. Hapus tugas')
        print('4. Keluar\n')

        user_input = input('pilih opsi: ')
        os.system('cls')

        if user_input == '1' or user_input.lower() == 'Lihat semua tugas':
            if task == []:
                print('Tolong tambahkan beberapa tugas!\n')
            else:
                print('\n++>TASK LIST<++')
                print(task)
        elif user_input == '2' or user_input.lower() == 'Tambah tugas':
            while True:
                print('input X jika sudah selesai menambah tugas\n')
                user_input2 = input('Input Tugas: ')
                
                if user_input2.lower() != 'x':
                    task.append(user_input2)

                if user_input2.lower() == 'x':
                    break
        elif user_input == '3' or user_input.lower() == 'Hapus tugas':
            if task == []:
                print('Jika ingin menghapus tugas, tolong pastikan anda sudah menambahkan beberapa tugas!\n')
            else:
                print('\n<=> TASK LIST <=>')
                print(task)
                print('\n=> CHOOSE OPTION <=')
                print('1. Hapus menggunakan index (mulai dari index 0)')
                print('2. Hapus menggunakan nilai / value')

                user_input3 = input('\ninput options: ')
                
                try:
                    if user_input3 == '1':
                        user_input4 = int(input('input index: '))
                        task.pop(user_input4)
                except:
                    print('index tersebut tidak ada dalam TASK LIST<++\n')

                try:  
                    if user_input3 == '2':
                        user_input5 = input('input value atau tugas yang ingin di hapus: ')
                        task.remove(user_input5)
                except:
                    print('value atau tugas tersebut tidak ada dalam TASK LIST<++')
        elif user_input == '4' or user_input.lower() == 'Keluar':
            print('\n===>>> PROGRAM END <<<===')
            print('===>>> THANKS AND GOODBYE <<<===')
            break
        else:
            print('pilih opsi atau input dengan benar!!')
except:
    print('ada kesalahan, diharapkan untuk input dengan benar, Terimakasih')