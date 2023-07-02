<div align="center">
  <h2>Idea about the program</h2>
</div>
<a>
  Most cars have a multimedia system. My car was no exception. The plan was to download songs to a USB flash drive. I downloaded them in the amount of 770 tracks. The trouble was that the multimedia system saw only 255 tracks. The problem is that the length of the string consists of ASCI characters. The only way to get around this problem is to distribute 770 tracks into folders so that each of them has no more than 255 tracks. It would seem that take and use CTRL+C CTRL+V. The problem with this method is that this method can be attributed to "slow algorithms" O^2. And if you also randomly mix, then this method can be safely attributed to "very slow algorithms" O! (Reference to the book <a href="https://edu.anarcho-copy.org/Algorithm/grokking-algorithms-illustrated-programmers-curious.pdf">"Grokking algorithms" Aditya Bhargava</a>). As you can understand, this is an actual problem for many motorists. To save yourself and others time in the future, it was decided to develop a console application in Python. Writing the code took less than an hour, and the help from him is enormous. 
</a>
<div align="center">
  <h2>About the program</h2>
</div>
<a>

The program implies three fields with data input:<br>
* In the first field, the user is asked to enter the path to the folder containing the tracks that need to be distributed into mini folders.
* In the second field, the user is asked to enter the path to the folder in which the program will create mini folders.
* In the third field, the user is asked for the number of mini folders.<br>

After the correct user input of data, the program begins its work. First of all, the program creates mini folders. They are called numbers from 0 to the number entered by the user. After that, the program receives a list of files in the tracks folder. Then, by randomly selecting a file, its new random location is determined. After the program determines and checks for exceeding the limit in the new mini tracks folder, the track is moved. After that, the program starts doing the same with the new file until the files run out.<br>

Disadvantages of the program:<br>
* The program distributes all files inside the folder into mini folders without exception. (But this is not a problem if the user puts all the tracks in a new folder in advance)
* There are problems with the program if the user tries to create mini folders inside the folder from which he takes tracks.
</a>
<div align="center">
  <h2>How do I start the program?</h2>
</div>
<a>

There are two options for how to run the program:<br>
* Download and run the file <a href="https://github.com/K1rsN7/music_distribution_for_cars/blob/main/random_file.exe">*"random_file.exe"*</a > on the computer.<br>
* Open file <a href="https://github.com/K1rsN7/music_distribution_for_cars/blob/main/random_file.py">*"random_file.py"*</a > in an IDE that supports the Python language.<br>

The program was made for the Windows operating system
</a>
<div align="center">
  <h2>Идея о программе</h2>
</div>
<a>
  В большинство авто присутствует мультимедийная система. Мой автомобиль не оказался исключением. В планах было скачать на USB-флешку песни. Я их скачал в количестве 770 треков. Беда заключалась в том, что мультимедийная система видела всего 255 треков. Проблема заключается в то длина строки состоит из ASCI символов. Единственный способ обойти эту проблему заключается в распределение 770 треков по папкам, чтобы в каждой из них было не больше 255 треков. Казалось бы, бери и используй CTRL+C CTRL+V. Проблема этого метода заключается в том, что данный способ можно относить к "медленным алгоритмам" O^2. А если же ещё случайным образом перемешивать, то данный способ можно смело относить к "очень медленным алгоритмам" O! (Отсылка на книгу <a href="https://en.ecomed.dgmu.ru/wp-content/uploads/2020/01/%D0%93%D1%80%D0%BE%D0%BA%D0%B0%D0%B5%D0%BC_%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B.pdf">"Грокаем алгоритмы" Адитья Бхаргава</a>). Как можно понять это актуальная проблемы для многих автолюбителей. Чтобы сэкономить себе и другим время в будущем было принято разработать консольное приложение на языке Python. Написание кода заняло меньше часа, а помощь от него колоссальная.
</a>
<div align="center">
  <h2>Об программе</h2>
</div>
<a>
  
  Программа подразумевает три поля с вводом данных:<br>
* В первое поле пользователя просят ввести путь к папке, в которой лежат треки, которые необходимо распределить по мини папкам.
* Во второе поле пользователя просят ввести путь к папке, в которой программа будет создавать мини папки.
* В третье поле пользователя просят количество мини папок.<br>

После корректного ввода пользователей данных программа начинает свою работу. Первым делом программа создает мини папки. Они называются числами от 0 до введённого пользователем числа. После чего программа получает список файлов в папке с треками. Затем путём случайного выбора файлу определяется его новое случайное место. После определения и проверки программой на превышение лимита в новой мини папке треков, трек перемещается. После программа начинает делать тоже самое с новым файлом до тех пор, пока не закончатся файлы.<br>

Недостатки программы:<br>
* Программа распределяет по мини папкам все файлы внутри папки без исключения. (Но это не является проблемой, если пользователь заранее поместит все треки в новую папку)
* Появляются проблемы с программой, если пользователь пытается внутри папки, из которой он берёт треки, создать мини папки.
</a>
<div align="center">
  <h2>Как запустить программу?</h2>
</div>
<a>
  
  Есть два варианта, как можно запустить программу:<br>
* Скачать и запустить файл <a href="https://github.com/K1rsN7/music_distribution_for_cars/blob/main/random_file.exe">*"random_file.exe"*</a> на компьютере.<br>
* Открыть файл <a href="https://github.com/K1rsN7/music_distribution_for_cars/blob/main/random_file.py">*"random_file.py"*</a> в IDE поддерживающий язык Python.<br>

Программа делалась под операционную систему Windows
</a>
<div align="center">
  <h2>Example of how the program works/Пример работы программы</h2>
  <img src="image1.png"/ >
  <img src="image2.png"/ >
  <img src="image3.png"/ >
  <img src="image4.png"/ >
</div>
