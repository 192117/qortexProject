from django.db import models


class Artist(models.Model):

    name = models.CharField(
        verbose_name='Название исполнителя',
        help_text='Введите название исполнителя',
        max_length=150,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Album(models.Model):

    name = models.CharField(
        verbose_name='Название альбома',
        help_text='Введите название альбома',
        max_length=150,
    )
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='album',
        verbose_name='Артисты',
        help_text='Выберите артистов, которые участвуют в записи этого альбома',
    )
    year = models.DateField(
        verbose_name='Год выпуска',
        help_text='Введите год выпуска альбома',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Song(models.Model):

    name = models.CharField(
        verbose_name='Название песни',
        help_text='Введите название песни',
        max_length=150,
    )
    info = models.ManyToManyField(
        Album,
        through='Track',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'


class Track(models.Model):

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='tracks',
        verbose_name='Альбом',
        help_text='Выберите альбом, в котором содержится данный трек',
    )
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name='tracks',
        verbose_name='Песня',
        help_text='Выберите песню, которая содержится в данном треке',
    )
    track_number = models.PositiveIntegerField(
        verbose_name='Порядковый номер в альбоме',
        help_text='Введите порядковый номер трека в альбоме',
        default=1,
    )

    def __str__(self):
        return f'{self.song}-{self.album}-{self.track_number}'

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'
