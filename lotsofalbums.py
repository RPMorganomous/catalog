from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from band_database_setup import Band, Base, AlbumItem, User

engine = create_engine('sqlite:///bandalbumswithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


Create dummy user
User1 = User(name="Metal Hunger", email="hungry@metal.com",
             picture='http://thekatynews.com/wp-content/uploads/2016/08/HSO-ROLLING-STONES.jpg')
session.add(User1)
session.commit()

# Band profile for Led Zeppelin
band1 = Band(user_id=1, name="Led Zeppelin", description="Led Zeppelin were an English rock band formed in London in 1968. The group consisted of guitarist Jimmy Page, singer Robert Plant, bassist and keyboardist John Paul Jones, and drummer John Bonham.", picture="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/LedZeppelinmontage.jpg/250px-LedZeppelinmontage.jpg")

session.add(band1)
session.commit()

albumItem1 = AlbumItem(user_id=1, name="Led Zeppelin", description="Featuring integral contributions from each of the group's four members, the album was recorded in October 1968 at Olympic Studios in London and established their fusion style of both blues and rock music.", price="$19.95", era="Roots", band=band1, year="1969", picture="https://coverartarchive.org/release-group/0f18ec88-aa87-38a9-8a65-f03d81763560/front.jpg")
session.add(albumItem1)
session.commit()


albumItem2 = AlbumItem(user_id=1, name="Led Zeppelin II", description="Incorporating several elements of blues and folk music, Led Zeppelin II exhibited the band's evolving musical style of blues-derived material and their guitar riff-based sound. It has been described as the band's heaviest album.", price="$19.95", era="Roots", band=band1, year="1969", picture="https://coverartarchive.org/release-group/33b4653d-006e-3cc1-8afb-386b15a6cd6e/front.jpg")
session.add(albumItem2)
session.commit()

albumItem3 = AlbumItem(user_id=1, name="Led Zeppelin III", description="This album represented a maturing of the band's music towards a greater emphasis on folk and acoustic sounds. It is widely acknowledged for showing that Led Zeppelin were more than just a conventional rock band.", price="$19.95", era="Roots", band=band1, year="1970", picture="https://coverartarchive.org/release-group/53f80f76-f8af-3558-bfd5-e7221e055c75/front.jpg")
session.add(albumItem3)
session.commit()

albumItem4 = AlbumItem(user_id=1, name="Led Zeppelin IV", description="Led Zeppelin IV was a commercial and critical success, featuring many of the band's best-known songs, including 'Black Dog', 'Rock and Roll', 'Going to California' and 'Stairway to Heaven'.", price="$19.95", era="Peak", band=band1, year="1971", picture="https://coverartarchive.org/release-group/2e61da88-39e9-3473-81d2-c964cb394952/front.jpg")
session.add(albumItem4)
session.commit()

albumItem5 = AlbumItem(user_id=1, name="Houses of the Holy", description="Containing some of the band's most famous songs, including 'The Song Remains the Same', 'The Rain Song', and 'No Quarter', Houses of the Holy became a commercial success, and was later certified 11x platinum.", price="$19.95", era="Peak", band=band1, year="1973", picture="https://coverartarchive.org/release-group/9b5006e5-b276-3a05-bcdd-8d986842320b/front.jpg")
session.add(albumItem5)
session.commit()

albumItem6 = AlbumItem(user_id=1, name="Physical Graffiti", description="Physical Graffiti was commercially and critically successful upon its release and debuted at number one on album charts in both the US and the UK. The album was later certified 16x platinum.", price="$19.95", era="Peak", band=band1, year="1975", picture="https://coverartarchive.org/release-group/116c9490-6af4-3827-8261-2d5b1f508fe7/front.jpg")
session.add(albumItem6)
session.commit()

albumItem7 = AlbumItem(user_id=1, name="Presence", description="It was written and recorded during a tumultuous time in the band's history, as singer Robert Plant was recuperating from serious injuries he had sustained the previous year in a car accident.", price="$19.95", era="Swan-Song", band=band1, year="1976", picture="https://coverartarchive.org/release-group/42f8acce-90fc-3471-a4cd-ace1ab816276/front.jpg")
session.add(albumItem7)
session.commit()

albumItem8 = AlbumItem(user_id=1, name="In Through the Out Door", description="Released by Swan Song Records, The album is a reflection of the personal turmoil that the band members had been going through before and during its recording.", price="$19.95", era="Swan-Song", band=band1, year="1979", picture="https://coverartarchive.org/release-group/2fbf4c3e-09e5-38f0-ae59-fbdc9ea16b87/front.jpg")
session.add(albumItem8)
session.commit()

albumItem9 = AlbumItem(user_id=1, name="Coda", description="The album is a collection of unused tracks from various sessions during Led Zeppelin's twelve-year career. It was released two years after the group had officially disbanded following the death of drummer John Bonham.", price="$19.95", era="Reformation", band=band1, year="1982", picture="https://coverartarchive.org/release-group/61de0438-6c34-363f-904e-b4d6267c79b9/front.jpg")
session.add(albumItem9)
session.commit()

# Band profile for Black Sabbath
band2 = Band(user_id=1, name="Black Sabbath", description="Black Sabbath are an English rock band, formed in Birmingham in 1968, by guitarist and main songwriter Tony Iommi, bassist and main lyricist Geezer Butler, singer Ozzy Osbourne, and drummer Bill Ward.", picture="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Sabs.jpg/250px-Sabs.jpg")

session.add(band2)
session.commit()

albumItem1 = AlbumItem(user_id=1, name="Black Sabbath", description="Although it was poorly received by most contemporary music critics at the time, Black Sabbath has since been credited as one of the most influential albums in the development of heavy metal music.", price="$19.95", era="Roots", band=band2, year="1970", picture="https://coverartarchive.org/release-group/826c9743-a3f0-3479-bf06-8df2e140ef1d/front.jpg")

session.add(albumItem1)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Paranoid", description="Paranoid contains several of the band's signature songs, including 'Iron Man', 'War Pigs' and the title track, which was the band's only Top 20 hit, reaching number 4 in the UK charts.", price="$19.95", era="Peak", band=band2, year="1970", picture="https://coverartarchive.org/release-group/cc053745-c447-3566-8f27-bed5438c9133/front.jpg")
session.add(albumItem2)
session.commit()

albumItem3 = AlbumItem(user_id=1, name="Master of Reality", description="It is widely regarded as the foundation of doom metal, stoner rock, and sludge metal. It was certified double platinum after having sold over 2 million copies.", price="$19.95", era="Peak", band=band2, year="1971", picture="https://coverartarchive.org/release-group/e51e9779-2edc-3b39-959c-299fdb5ed940/front.jpg")
session.add(albumItem3)
session.commit()

albumItem4 = AlbumItem(user_id=1, name="Vol 4", description=" It was the first album by Black Sabbath not produced by Rodger Bain; guitarist Tony Iommi assumed production duties. Patrick Meehan, the band's then-manager, was listed as co-producer.", price="$19.95", era="Peak", band=band2, year="1974", picture="https://coverartarchive.org/release-group/8c292627-3459-3852-8ebc-226c12db175d/front.jpg")
session.add(albumItem4)
session.commit()

albumItem5 = AlbumItem(user_id=1, name="Sabbath Bloody Sabboth", description="It was produced by the band and recorded at Morgan Studios in London in September 1973.", price="$19.95", era="Peak", band=band2, year="1973", picture="https://coverartarchive.org/release-group/dd9bd473-0232-3a12-b51e-742de1aca5ca/front.jpg")
session.add(albumItem5)
session.commit()

albumItem6 = AlbumItem(user_id=1, name="Sabotage", description="It was recorded in the midst of litigation with their former manager Patrick Meehan and the stress that resulted from the band's ongoing legal woes infiltrated the recording process, inspiring the album's title.", price="$19.95", era="Swan-Song", band=band2, year="1975", picture="https://coverartarchive.org/release-group/8ef6fc58-d87a-46cf-ab9d-077291784ada/front-250.jpg")
session.add(albumItem6)
session.commit()

albumItem7 = AlbumItem(user_id=1, name="Technical Ecstasy", description="The album was certified Gold on 19 June 1997 and peaked at number 51 on the Billboard 200 Album chart.", price="$19.95", era="Swan-Song", band=band2, year="1976", picture="https://coverartarchive.org/release-group/de117377-2f09-3502-8959-e1eca1b583a8/front.jpg")
session.add(albumItem7)
session.commit()

albumItem8 = AlbumItem(user_id=1, name="Never Say Die!", description="It was the last studio album with the band's original lineup and also the last studio album to feature original vocalist Ozzy Osbourne until 2013's 13.", price="$19.95", era="Swan-Song", band=band2, year="1978", picture="https://coverartarchive.org/release-group/eb8c8e6c-b554-31d3-bae0-1c4ea64336d0/front-250.jpg")
session.add(albumItem8)
session.commit()

albumItem9 = AlbumItem(user_id=1, name="Reunion", description="It features the original line-up of Ozzy Osbourne, Tony Iommi, Geezer Butler and Bill Ward, the first recording of the four musicians together after the firing of Osbourne in 1979.", price="$19.95", era="Reformation", band=band2, year="1998", picture="https://coverartarchive.org/release-group/5048cda8-4269-3226-a289-71ef84c3ff0e/front-250.jpg")
session.add(albumItem9)
session.commit()

# Band profile for Deep Purple
band3 = Band(user_id=1, name="Deep Purple", description="Deep Purple are an English rock band formed in Hertford in 1968. They are considered to be among the pioneers of heavy metal and modern hard rock.", picture="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Deep_Purple_in_2004.jpg/250px-Deep_Purple_in_2004.jpg")

session.add(band3)
session.commit()

albumItem1 = AlbumItem(user_id=1, name="Shades of Deep Purple", description="Stylistically the music is close to psychedelic rock and progressive rock, two genres with an ever-growing audience in the late 1960s.", price="$19.95", era="Roots", band=band3, year="1968", picture="https://coverartarchive.org/release-group/bdb083d6-be5e-32b3-97df-3d899a8ff858/front.jpg")
session.add(albumItem1)
session.commit()


albumItem2 = AlbumItem(user_id=1, name="The Book of Taliesyn", description="The music style is a mix of psychedelic rock, progressive rock and hard rock, with several inserts of classical music arranged by the band's keyboard player Jon Lord.", price="$19.95", era="Roots", band=band3, year="1968", picture="https://coverartarchive.org/release-group/3a2bbe30-d2c7-367b-9326-f0082adad661/front.jpg")
session.add(albumItem2)
session.commit()

albumItem3 = AlbumItem(user_id=1, name="Deep Purple", description="It was the last album with the original line-up due to conflicts over whether the band should continue in their rawer, heavier direction.", price="$19.95", era="Roots", band=band3, year="1969", picture="https://coverartarchive.org/release-group/bacc3ccf-32aa-3103-b50c-4edaa35e6fb6/front-250.jpg")
session.add(albumItem3)
session.commit()

albumItem4 = AlbumItem(user_id=1, name="Deep Purple in Rock", description="It was the first studio album recorded by the classic Mark II line-up. Rod Evans (vocals) and Nick Simper (bass) had been fired in June 1969 and were replaced by Ian Gillan and Roger Glover, respectively.", price="$19.95", era="Roots", band=band3, year="1970", picture="https://coverartarchive.org/release-group/ebdb53c3-fbae-34b1-81cb-f825c9a56822/front-250.jpg")
session.add(albumItem4)
session.commit()

albumItem5 = AlbumItem(user_id=1, name="Fireball", description="The second with the classic Mk II line-up. It was recorded at various times between September 1970 and June 1971.", price="$19.95", era="Roots", band=band3, year="1971", picture="https://coverartarchive.org/release-group/b9547871-240a-3ca4-97d7-9f2dfffe471c/front-250.jpg")
session.add(albumItem5)
session.commit()

albumItem6 = AlbumItem(user_id=1, name="Machine Head", description="Machine Head is often cited as a major influence in the early development of the heavy metal music genre. Commercially, it is Deep Purple's most successful album.", price="$19.95", era="Peak", band=band3, year="1972", picture="https://coverartarchive.org/release-group/d00243c5-adcf-3018-9aa7-1957d7a5a774/front-250.jpg")
session.add(albumItem6)
session.commit()

albumItem7 = AlbumItem(user_id=1, name="Who Do We Think We Are", description="Showeing a move to a more blues based sound, Deep Purple's last album with singer Ian Gillan and bassist Roger Glover until Perfect Strangers came out in 1984.", price="$19.95", era="Swan-Song", band=band3, year="1973", picture="https://coverartarchive.org/release-group/edba2b6f-8f50-3bc9-b2ac-1df8bdb51daa/front-250.jpg")
session.add(albumItem7)
session.commit()

albumItem8 = AlbumItem(user_id=1, name="Burn", description="This was the first Deep Purple album to feature then-unknown David Coverdale on vocals and Glenn Hughes from Trapeze on bass and vocals.", price="$19.95", era="Swan-Song", band=band3, year="1974", picture="https://coverartarchive.org/release-group/e8459360-b0d1-331e-a1e7-9717c962d29f/front-250.jpg")
session.add(albumItem8)
session.commit()

albumItem9 = AlbumItem(user_id=1, name="Stormbringer", description="On this album, the soul and funk elements that were only hinted at on Burn are much more prominent.", price="$19.95", era="Swan-Song", band=band3, year="1974", picture="https://coverartarchive.org/release-group/95d17f98-dfe2-36c4-b950-fcdc1bdbc279/front-250.jpg")
session.add(albumItem9)
session.commit()

albumItem10 = AlbumItem(user_id=1, name="Come Taste The Band", description="It is the only Deep Purple studio record featuring Tommy Bolin, who replaced Ritchie Blackmore on guitar and is also the final of three albums to feature Glenn Hughes on bass and David Coverdale on lead vocals, before he later left to form Whitesnake.", price="$19.95", era="Swan-Song", band=band3, year="1975", picture="https://coverartarchive.org/release-group/d12f085d-7861-36cd-a2fb-55a18ddc6e56/front-250.jpg")
session.add(albumItem10)
session.commit()

albumItem11 = AlbumItem(user_id=1, name="Perfect Strangers", description="It was the first Deep Purple studio album in nine years, and the first with the Mk II line-up in eleven years, the last being Who Do We Think We Are in 1973.", price="$19.95", era="Reformation", band=band3, year="1984", picture="https://coverartarchive.org/release-group/41a276ce-ea2b-377c-9ad8-0ef0bfd1f5c2/front-250.jpg")
session.add(albumItem11)
session.commit()


print "Bands and albums successfully imported!"

