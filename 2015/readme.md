# Заметки к задачам 2015 года

## День 15

Спасибо дню 04 2019 года :smile:
Идею того, как **эффективно** разбить 100 ложек на 4 группы взял из **неработающего** (неработающего, Карл) решения.

## День 19

Двоякое впечатление:

* С одной стороны, я нашел правильную идею, работающую на малых данных.
* С другой стороны, на больших данных она работает не очень чтобы уж, слишком долго.
  Прочитанная на днях идея о том, что линейные алгоритмы лучше, подтверждается.

Решение, которое работает, использует идею стека из решения @emilyskidsister.
Основная идея этого решения такая же, что и у меня, но она реализована через стек и линейный проход, а не через рекурсию.

Так что я и решил, и не решил вторую звездочку. Как-то так.

## День 21

Тут творилась какая-то мистика.
Написанный мной код выдавал все, что угодно, кроме правильного ответа.
Но когда я последовал примеру @emilyskidsister и явно задал пустые кольца и доспехи, отказавшись от кортежей переменной длины (я пытался сначала динамически высчитывать их размер), все заработало.
Либо что-то в недрах питона не давало коду работать, либо просто не надо выпендриваться и делать по-простому.

Задачу я сам себе засчитываю, так как за исключением вышеуказанной идеи все остальное у меня было изначально аналогично коду @emilyskidsister.
Говорили мне в свое время: сначала напиши как-нибудь, а потом уж оптимизируй.

## День 24

Признаюсь честно -- я подсмотрел идею использования itertools на реддите.
Тяга к велосипедам тянула меня в ненужную сторону. Нет, оно бы сработало, но через долгое время.

Еще один урок: иногда для получения ответа не нужно получать предельно полный ответ на промежуточные задачи.
Иногда достаточно получить часть полного ответа, достаточную для решения.
