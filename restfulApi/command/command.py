import click, json
from restfulApi import app, db
from restfulApi.model.Music import Music
from restfulApi.model.Artist import Artist


@app.cli.command()
@click.option('-a', '--artist', default=False)
@click.option('-m', '--music', default=False)
@click.option('-both', default=True)
@click.option('--count', default=20)
def forge(count, artist, music, both):
    from faker import Faker
    db.drop_all()
    db.create_all()
    fake = Faker(locale='zh_CN')
    click.echo("Now generating fake data...")
    for i in range(count):
        if both:
            musicData = Music(
                name=fake.sentence(),
                author=fake.name(),
                publish_time=fake.date_time_this_year())
            artistData = Artist(
                name=fake.name(),
                birth=fake.date_time_this_year(),
                city=fake.city()
            )
            db.session.add(musicData)
            db.session.add(artistData)
            click.echo('Generating %d fake music and artist ' % i)
        elif artist:
            artistData = Artist(
                name=fake.name(),
                birth=fake.date_time_this_year(),
                city=fake.city()
            )
            click.echo('Generating %d fake artist ' % i)
            db.session.add(artistData)
        elif music:
            musicData = Music(
                name=fake.sentence(),
                author=fake.name(),
                publish_time=fake.date_time_this_year())
            db.session.add(musicData)
            click.echo('Generating %d fake music' % i)
    db.session.commit()
    click.echo('Generated %d fake music %s %s' % (count, artist, music))


@app.cli.command()
def query():
    musics = Music.query.order_by(Music.publish_time.desc()).all()
    artist = Artist.query.order_by(Artist.id.desc()).all()
    ret = {
        'music': [m.serialize() for m in musics],
        'artist': [m.serialize() for m in artist]
    }
    # click.echo(ret)
    click.echo(json.dumps(ret).encode('utf-8').decode("unicode_escape"))
