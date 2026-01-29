
options=('1. Add a task',
         '2. Remove a task',
         '3. View tasks',
         'q to quit')
tasks=[]
running=True
entering_task=True
# viewing_tasks=True

while running:
    print('------MENU------')
    for option in options:
        print(option)
    print('----------------')
    inputs=input('INPUT: ')
    if inputs=='q':
        running=False

    elif int(inputs)==1:
        print('----------ENTERING A TASK----------------')
        while  True:
            task=input('Enter a task(q to Return to Menu): ')
            if task=='q':
                break
            else:
                tasks.append(task)
    
    elif int(inputs)==3:
        while True:
            print('----------------YOUR TASKS---------------')
            for x,y in enumerate(tasks,1):
                print(f'{x} : {y}')
        
            task=input('Press any key to Return To Menu')
            if task=='q':
                break
    
    elif int(inputs)==2:
         print('----------DELETE TASK------------')
         while True:
            if len(tasks)==0:
                print('No Tasks')
                break
            for x,task in enumerate(tasks,1):
                 print(f'{x}: {task}')
            choice=input('Delete Task no.: ')

            index=int(choice)-1

            if 0<=index<=len(tasks):
                tasks.pop(index)
            else:
                print('invalid choice')
            
            
            
            
                 
            
                
        





