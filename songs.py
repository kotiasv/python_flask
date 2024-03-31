from flask import Flask
from models.songs import Artist, Album, Song
from dbinit import db

app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

db.init_app(app)
with app.app_context():
    db.create_all()

    artist1 = Artist(name="camellia")
    artist2 = Artist(name="dennsgh")
    artist3 = Artist(name="dj-Jo")
    db.session.add_all([artist1, artist2, artist3])
    db.session.commit()
    album1 = Album(title='U.U.F.O', year='2021', artist=artist1)
    album2 = Album(title='202X Legacy', year='2024', artist=artist1)
    album3 = Album(title='League of Legends Collection', year='2020', artist=artist2)
    album4 = Album(title='Future Bass Side of View', year='2018', artist=artist2)
    album5 = Album(title='Anime Remixes', year='2021', artist=artist3)
    db.session.add_all([album1, album2, album3, album4, album5])
    db.session.commit()
    song1 = Song(title='Bermuda Triangle', length='4:03', track_number=1, album=album1)
    song2 = Song(title='GHOUL', length='4:35', track_number=2, album=album1)
    song3 = Song(title='Myths You Forgot', length='4:18', track_number=3, album=album1)
    song4 = Song(title='Hello (BPM) 2021', length='2:22', track_number=1, album=album2)
    song5 = Song(title='Hello (BPM) 2022', length='2:30', track_number=2, album=album2)
    song6 = Song(title='Hello (BPM) 2023', length='2:48', track_number=3, album=album2)
    song7 = Song(title='Hello (BPM) 2024', length='3:05', track_number=4, album=album2)
    song8 = Song(title='MORE', length='2:51', track_number=1, album=album3)
    song9 = Song(title='THE BADDEST', length='3:39', track_number=2, album=album3)
    song10 = Song(title='POPSTARS', length='2:16', track_number=3, album=album3)
    song11= Song(title='hot girl bummer remix', length='2:32', track_number=1, album=album4)
    song12 = Song(title='sunkissed days', length='3:15', track_number=2, album=album4)
    song13 = Song(title='Kimetsu no Yaiba', length='4:53', track_number=1, album=album5)
    song14 = Song(title='Konomi Suzuki', length='4:45', track_number=2, album=album5)
    song15 = Song(title='Stay Alive', length='3:50', track_number=3, album=album5)
    db.session.add_all([song1, song2, song3, song4, song5, song6, song7, song8, song9, song10, song11, song12, song13, song14, song15])
    db.session.commit()