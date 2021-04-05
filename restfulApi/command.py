import click

from restfulApi import app, db
from restfulApi.model.Music import Music
from restfulApi.model.Artist import Artist


@app.cli.command()
@click.option('-a', '--artist', default=False)
@click.option('-m', '--music', default=False)
@click.option('-all', default=True)
@click.option('--count', default=20)
def forge(count, artist, music, all):
    from faker import Faker
    db.drop_all()
    db.create_all()
    fake = Faker(locale='zh_CN')
    click.echo("Now generating fake data...")
    for i in range(count):
        if all:
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


