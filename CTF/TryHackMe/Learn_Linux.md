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
 
Answer format: **** ** *****
