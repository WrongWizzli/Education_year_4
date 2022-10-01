# Geometry-Wars
Простой аналог игры Geometry Wars.

Управление:
1) Перемещение - стрелочки на клавиатуре
2) Стрельба - левая кнопка мыши (стрельба ведется в направлении курсора)
3) Выход из игры - клавиша Esc.


Что есть в игре:
Ограниченное поле, по которому может перемещаться игрок. По ходу игры регулярно появляются мобы (стрелки, простые преследователи и крутящиеся объекты, которые 
просто отскакивают от стен). Они все имеют свое количество здоровья и другие характеристики, которые растут со временем игры. Кроме врагов, в игре есть и бонусы на
увеличение урона и здоровья игрока (шанс выпадения бонуса 3%, появления монстра - 97%). Здоровье игрока отображается в правом верхнем углу. Игра заканчивается, когда здоровье опускается до нуля.

За каждого убитого моба начисляется определенное количество очков в зависимости от его типа и времени в игре. Суммарный счет выводится на экран.

Для простоты просмотра игры параметры игрока выставлены на запредельный уровень (все мобы ваншотятся + скорость стрельбы очень высока).


Как запустить: запустить скрипт build.sh, далее запустить game бинарник.

Чего может не хватать для сборки проекта:
1) C++, cmake
2) libx11-dev