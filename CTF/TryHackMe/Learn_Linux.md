# Learn Linux
A guided room designed to teach you the Linux basics!

# [Task 1] Intro 28/01/2020
This room is designed to teach you about linux concepts, and tools.

Because of this, this room expects no prior knowledge. The only expectation this room has is an eagerness to learn, and a willingness to google if your stuck :).

This room has a natural flow to it; however if you are experienced in linux, and just want a refresher on a specific topic, you can jump around as need be.

## #1	Read the above.
No answer needed
 
# [Task 2] Methodology 18/02/2020
After careful consideration, I've deemed the best way to go about this is to introduce various concepts in sections, with each section being more complex and requiring knowledge from the previous section. To better enable the transition between section, I've split each section into different users in the VM; when you finish a section you'll have to complete a challenge and then you'll be able to move onto the next section.

## #1	Read the above.
No answer needed

# [Task 3] [Section 1: SSH] - Intro 28/01/2020
SSH is the act of remotely accessing a machine. SSH allows you to run commands interactively on the remote machine. This is done through the use of a program on the target machine, which allows the ssh client to interface with the target host.

While the most common usage of a regular operating system is graphical(allowing you to see pictures, web browsers, file managers etc.) SSH works through a command line, meaning anything done on the target machine will be done through a command prompt similar to this.


It may look intimidating at first, but you'll soon find out you can do much of the same functionality that you're able to do using graphical user interfaces!

 It is an invaluable tool, and how you will be accessing this machine to learn and to do the challenges. Depending on the operating system there are different ways of SSHing into a machine. This section will purely focus on the windows way(PuTTY), and after we learn more about linux commands, and how they work, we'll return back to this section and learn about the linux method.

## #1	Read the above
No answer needed

# [Task 6] [Section 2: Running Commands] - Manual Pages and Flags 13/02/2020
Most of the commands you'll learn about have a lot of options that are not immediately known at first glance, these options are known as flags, and have the format <command> <flag> <input>. These flags can be learned about using the man command. The man command has the format man <command>. Therefore, to learn about flags for the echo command, we would type man echo. Typing that shows us a nicely formatted document:

We get alot of information, but the flags are stored in the description section. For example the flag to remove the newline is -n. So to output "Shiba" without the newline you would type echo -n Shiba.        

Note: Some commands support the -h flag, meaning you can type <command> -h and get a list of flags and other useful information without using man.           

## #1	How would you output hello without a newline
 
Answer format: **** ** *****<p>
Answer format: echo -n Hello

# [Task 7] [Section 3: Basic File Operations] - ls 13/02/2020
ls is a command that lists information about every file/directory in the directory. Just running the ls command outputs the name of every file in the directory.

As with other commands ls has many flags that can manipulate the output.  For example ls -a shows all files/directories including ones that start with .

### #1	What flag outputs all entries
 
Answer format: -a
### #2	What flag outputs things in a "long list" format    
Answer format: -l

# [Task 8] [Section 3: Basic File Operations] - cat 18/02/2020
cat short for concatenate, does exactly that, it outputs the contents of files to the console. For example, given a file called a.txt which contains the data "hello", cat a.txt would output hello.

Note: cat supports the --help flag meaning that you can see useful flags without going to the man page!

### #1	What flag numbers all output lines?    

Answer format: -n<p>
 
# [Task 9] [Section 3: Basic File Operations] - touch 18/02/2020
touch is a pretty simple command, it creates files. Given the command touch b.txt, b.txt would be created.
### #1	Read the above!
 
No answer needed

# [Task 10] [Section 3: Basic File Operations] - Running A Binary 18/02/2020
Occasionally there will be times when you want to run downloaded or user created programs. This is done by providing the full path to the binary, for example say you download a binary that outputs not, providing the full path to that binary will execute it. 

This seems like a good time to mention Relative Paths! Every time you intend on running the binary, you don't need to provide a full path, you can use Relative Paths.

Relative Paths:

The chart below will assume the current path is /tmp/aa 

### #1	How would you run a binary called hello using the directory shortcut . ?

Answer format: ./hello

### #2	How would you run a binary called hello in your home directory using the shortcut ~ ?

Answer format: ~/Hello

### #3	How would you run a binary called hello in the previous directory using the shortcut .. ?

Answer format: ../Hello

# [Task 11] Binary - Shiba1 18/02/2020
Now that you've learned basic file operations, you can solve the first challenge! This challenge is pretty simple, create a file called noot.txt.

Once you're done run the binary and you'll be given the password for the user shiba2!

### #1	What's the password for shiba2        
<p> 
Answer format: ********<p>
Answer format: pinguftw<p>
haciendo strings sobre el fichero binario puedes comprobar que hace un cat /etc/shiba/shiba2, el programa comprueba que existe el fichero noot.txt y si es así te hace un cat.

# [Task 12] su 18/02/2020
Now that we have our next user password, it seems like a good time to cover su. su is a command that allows you to change the user, without logging out and logging back in again. For example if you wanted to switch to shiba2 while you're the user shiba1, you would type su shiba2 . You would then be prompted for a password and if you entered shiba2's password you would then become shiba2

Note: Typing su on its own is equivalent to typing su root. 

### #1	How do you specify which shell is used when you login?    
 
Answer format: -s

Dejo de escribir porque es tan sencillo que pierdo más el tiempo en hacer eśto que en terminar la máquina.

Última tarea, es la única complicada.
Hay que hacer un find, buscando ficheros de usuarios que tenemos acceso, shiba[1-4]. Te tocara usar sudo -l :D #Enjoy
