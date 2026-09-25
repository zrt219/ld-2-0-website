# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.error
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

VIDEO_URL = 'https://lornettedaye.com/campaigns/curacao/curacao-full-highlights.mp4'

posts_data = [
    {
        "id": 1,
        "type": "video",
        "slot": "Friday 6:30 AM MDT (Sep 25, 2026)",
        "dueAt": "2026-09-25T12:30:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "WAKE UP TO THE GREATEST COMEBACK IN CARIBBEAN HISTORY! 🇨🇼🌊\n\n"
            "Costa Rica 3, Curaçao 0 at halftime.\n\n"
            "Then the second half exploded. Kenji Gorré cuts the deficit. "
            "Tahith Chong levels the psychological momentum. "
            "Gorré strikes again for the brace. "
            "Jordi Paulina puts in the 88th-minute winner.\n\n"
            "Final score: 4-3 for Curaçao!\n\n"
            "To everyone waking up across Willemstad, the Netherlands, and the entire diaspora: "
            "play this with the volume on full blast today!\n\n"
            "Ban Kòrsou!\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Executive mindset coaching and keynote speaking: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #LornetteDaye"
        )
    },
    {
        "id": 2,
        "type": "video",
        "slot": "Friday 8:30 AM MDT (Sep 25, 2026)",
        "dueAt": "2026-09-25T14:30:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "HOW LOUD DID YOU ROAR WHEN THE FOURTH GOAL WENT IN? 🇨🇼⚽\n\n"
            "Look at the full sequence from start to finish.\n\n"
            "When you are on the road in San José against a regional powerhouse, trailing 3-0, "
            "human nature says protect the scoreline. But Team Curaçao chose belief.\n\n"
            "They showed what Caribbean heart and tactical courage look like under pressure.\n\n"
            "Drop your neighborhood or city in the comments if you cheered for Kòrsou today! "
            "Dushi Kòrsou forever.\n\n"
            "Explore Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Book Coach Lornette Daye for your next conference: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanSports #IslandFootball #SmallIslandBigDreams #CaribbeanExcellence #LornetteDaye"
        )
    },
    {
        "id": 3,
        "type": "video",
        "slot": "Friday 11:15 AM MDT (Sep 25, 2026)",
        "dueAt": "2026-09-25T17:15:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "LUNCHTIME FILM STUDY: KENJI GORRÉ AND TAHITH CHONG LEADING THE CHARGE 🌊🇨🇼\n\n"
            "Watch the speed of thought in transition.\n\n"
            "Gorré finding the pocket. Chong demanding the ball and shifting the balance of the match. "
            "This is not luck; this is elite execution delivered with cold-blooded composure "
            "when everything was on the line.\n\n"
            "Who was your player of the match? Let us settle the debate in the comments!\n\n"
            "Ban Kòrsou!\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Bring Olympic mental discipline to your organization: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanPower #CaribbeanToTheWorld #SmallIslandBigDreams #LornetteDaye"
        )
    },
    {
        "id": 4,
        "type": "video",
        "slot": "Friday 1:45 PM MDT (Sep 25, 2026)",
        "dueAt": "2026-09-25T19:45:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Championship Library ($14.99 CAD) & Speaking",
        "text": (
            "160,000 PEOPLE. ONE UNSTOPPABLE BLUE WAVE. 🇨🇼⚡\n\n"
            "Never let anyone tell you that size defines your ceiling.\n\n"
            "A small Caribbean island went into Central America and delivered a performance "
            "that reverberated around the international football world.\n\n"
            "From Bandabou to Banda'riba, every street was celebrating. "
            "Share this full highlight reel with a proud Curaçaoan today!\n\n"
            "Nos ta Kòrsou!\n\n"
            "Explore Coach Lornette Daye's complete digital library ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote bookings and high-performance seminars: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #VamosCuraçao #CuraçaoFootball #CaribbeanPride #IslandPride #SmallIslandBigDreams #CaribbeanAthletes #LornetteDaye"
        )
    },
    {
        "id": 5,
        "type": "video",
        "slot": "Friday 6:00 PM MDT (Sep 25, 2026)",
        "dueAt": "2026-09-26T00:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "FRIDAY NIGHT PRIME TIME: RELIVE THE 3-0 TO 4-3 MIRACLE 🇨🇼🏆\n\n"
            "Turn this up. Watch the raw emotion on the bench and the fire on the pitch.\n\n"
            "When you go down 3-0, you discover what your culture is truly built on. "
            "Curaçao did not blink. They played with freedom, passion, and tactical sharpness "
            "until the final whistle blew.\n\n"
            "Tag someone who needs a reminder of what pure perseverance looks like!\n\n"
            "Ban Kòrsou!\n\n"
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Executive coaching with Coach Lornette Daye: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanExcellence #SmallIslandBigDreams #IslandFootball #LornetteDaye"
        )
    },
    {
        "id": 6,
        "type": "video",
        "slot": "Friday 9:15 PM MDT (Sep 25, 2026)",
        "dueAt": "2026-09-26T03:15:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "FRIDAY NIGHT FINALE: CELEBRATING THE HEROES OF KÒRSOU 🇨🇼🎉\n\n"
            "What an unforgettable night in island football history.\n\n"
            "Kenji Gorré with the double. Tahith Chong with the masterclass. "
            "Jordi Paulina with the ice in his veins. "
            "Every tackle, every save, every pass told a story of national dignity and self-belief.\n\n"
            "Where were you watching when history was made? Drop your story below! "
            "Dushi Kòrsou to the world!\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Bring Coach Lornette to your leadership retreat: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanPride #CaribbeanToTheWorld #SmallIslandBigDreams #CaribbeanPower #LornetteDaye"
        )
    },
    {
        "id": 7,
        "type": "video",
        "slot": "Saturday 11:00 AM MDT (Sep 26, 2026)",
        "dueAt": "2026-09-26T17:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "SATURDAY MORNING REMINDER: THE BLUE WAVE NEVER QUITS 🌊🇨🇼\n\n"
            "Pour your coffee and watch this 3-minute masterclass.\n\n"
            "Down 3-0 at the half on hostile ground. Most squads would surrender. "
            "Team Curaçao walked out of the tunnel with heads high and hearts on fire. "
            "Four goals later, history was rewritten.\n\n"
            "Ban Kòrsou!\n\n"
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Book Lornette Daye for your athletic or corporate summit: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #Korsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #LornetteDaye"
        )
    },
    {
        "id": 8,
        "type": "video",
        "slot": "Saturday 5:30 PM MDT (Sep 26, 2026)",
        "dueAt": "2026-09-26T23:30:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "SATURDAY NIGHT FOOTBALL PASSION: DIASPORA PRIDE UNLEASHED 🇨🇼🔥\n\n"
            "From Willemstad to Rotterdam, Amsterdam to North America, "
            "the roar of the Curaçao diaspora shook the room when Paulina buried the fourth goal.\n\n"
            "Football is more than a game; it is an identity. "
            "It is proof of what happens when a collective family stands together. "
            "Shout out your city in the comments!\n\n"
            "Ban Kòrsou!\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "High-performance coaching and leadership programs: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanSports #IslandFootball #SmallIslandBigDreams #CaribbeanExcellence #LornetteDaye"
        )
    },
    {
        "id": 9,
        "type": "video",
        "slot": "Sunday 10:00 AM MDT (Sep 27, 2026)",
        "dueAt": "2026-09-27T16:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "SUNDAY MORNING INSPIRATION: RISING FROM THE ASHES 🇨🇼⚽\n\n"
            "When the first half went wrong, Team Curaçao did not point fingers.\n\n"
            "They adjusted their communication, tightened their spacing, and backed one another on every run. "
            "That is how you turn a 0-3 deficit into a 4-3 triumph. "
            "Share this lesson with your family or team today.\n\n"
            "Dushi Kòrsou!\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote speaking and executive development: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanPower #CaribbeanToTheWorld #SmallIslandBigDreams #LornetteDaye"
        )
    },
    {
        "id": 10,
        "type": "video",
        "slot": "Sunday 6:00 PM MDT (Sep 27, 2026)",
        "dueAt": "2026-09-28T00:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "SUNDAY NIGHT REPLAY: JORDI PAULINA'S 88TH MINUTE COLD FINISH 🇨🇼⚡\n\n"
            "Look at the composure.\n\n"
            "88th minute. The score is 3-3. The entire stadium holding its breath. "
            "Paulina receives, positions his body, and strikes with absolute certainty. "
            "That is the moment legends are made.\n\n"
            "Who screamed the loudest in your house? Tell us below!\n\n"
            "Ban Kòrsou!\n\n"
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Corporate workshops and Olympic mindset consulting: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #VamosCuraçao #CuraçaoFootball #CaribbeanPride #IslandPride #SmallIslandBigDreams #CaribbeanAthletes #LornetteDaye"
        )
    },
    {
        "id": 11,
        "type": "video",
        "slot": "Monday 9:00 AM MDT (Sep 28, 2026)",
        "dueAt": "2026-09-28T15:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "START YOUR WEEK LIKE TEAM CURAÇAO: REFUSE TO ACCEPT DEFEAT 🌊🇨🇼\n\n"
            "Monday morning mindset:\n\n"
            "Whatever deficit you face, whatever challenges sit on your desk, "
            "remember what 10 men from Curaçao did when the world counted them out at 3-0. "
            "They fought. They executed. They won 4-3. "
            "Step into your week with that exact championship posture.\n\n"
            "Ban Kòrsou!\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Book Coach Lornette Daye for your team: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanExcellence #SmallIslandBigDreams #IslandFootball #LornetteDaye"
        )
    },
    {
        "id": 12,
        "type": "video",
        "slot": "Monday 5:00 PM MDT (Sep 28, 2026)",
        "dueAt": "2026-09-28T23:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "MONDAY NIGHT TAPE: THE ARCHITECTURE OF A COMEBACK 🇨🇼🎯\n\n"
            "Study how Curaçao turned the tide.\n\n"
            "Goal 1: Ignite the belief.\n"
            "Goal 2: Equalize the psychological pressure.\n"
            "Goal 3: Level the score.\n"
            "Goal 4: Complete the conquest.\n\n"
            "Step by step, possession by possession. "
            "What goal was the most breathtaking in your view? "
            "Dushi Kòrsou!\n\n"
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "High-performance executive coaching: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanPride #CaribbeanToTheWorld #SmallIslandBigDreams #CaribbeanPower #LornetteDaye"
        )
    },
    {
        "id": 13,
        "type": "video",
        "slot": "Tuesday 9:00 AM MDT (Sep 29, 2026)",
        "dueAt": "2026-09-29T15:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "TACTICAL DISCIPLINE UNDER HOSTILE PRESSURE 🇨🇼⚽\n\n"
            "In the heart of San José, Costa Rica, against a roaring home crowd, "
            "Team Curaçao kept their composure. They did not lash out. They did not panic. "
            "They stayed committed to their system and let their football do the talking.\n\n"
            "Drop a blue flag in the comments if you are proud of how this squad represented the island!\n\n"
            "Ban Kòrsou!\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Bring Lornette Daye to your next conference: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #Korsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #LornetteDaye"
        )
    },
    {
        "id": 14,
        "type": "video",
        "slot": "Tuesday 5:00 PM MDT (Sep 29, 2026)",
        "dueAt": "2026-09-29T23:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "TAHITH CHONG: PURE CLASS ON THE INTERNATIONAL STAGE 🌊🇨🇼\n\n"
            "Watch Chong glide past defenders and open up the Costa Rican backline.\n\n"
            "His vision and poise gave Curaçao the exact momentum shift they needed. "
            "Great players rise in great moments. "
            "Tag a young footballer who needs to study this tape today!\n\n"
            "Ban Kòrsou!\n\n"
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Corporate leadership workshops and keynotes: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanSports #IslandFootball #SmallIslandBigDreams #CaribbeanExcellence #LornetteDaye"
        )
    },
    {
        "id": 15,
        "type": "video",
        "slot": "Wednesday 9:00 AM MDT (Sep 30, 2026)",
        "dueAt": "2026-09-30T15:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Championship Library ($14.99 CAD) & Speaking",
        "text": (
            "WEDNESDAY WORKOUT FUEL: RUN LIKE YOU ARE PLAYING FOR KÒRSOU 🇨🇼⚡\n\n"
            "Need energy for your training today? Put this full highlight video on.\n\n"
            "Look at the work rate in the 85th minute. Sprints, tackles, headers, recovery runs. "
            "Nobody gave up an inch. "
            "That is the standard of excellence we preach every single day.\n\n"
            "Ban Kòrsou!\n\n"
            "Explore Coach Lornette Daye's full book catalog ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote speaking inquiries: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanPower #CaribbeanToTheWorld #SmallIslandBigDreams #LornetteDaye"
        )
    },
    {
        "id": 16,
        "type": "video",
        "slot": "Wednesday 5:00 PM MDT (Sep 30, 2026)",
        "dueAt": "2026-09-30T23:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "A WIN FOR EVERY CARIBBEAN NATION 🇨🇼🌴\n\n"
            "When Curaçao wins like this, all of the Caribbean stands tall.\n\n"
            "It shows the world the extraordinary talent, resilience, and tactical intelligence "
            "present throughout our region. "
            "To our brothers and sisters across Jamaica, Trinidad, Barbados, Suriname, and beyond: "
            "thank you for the love and solidarity!\n\n"
            "Nos ta Kòrsou!\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Executive mindset training: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #VamosCuraçao #CuraçaoFootball #CaribbeanPride #IslandPride #SmallIslandBigDreams #CaribbeanAthletes #LornetteDaye"
        )
    },
    {
        "id": 17,
        "type": "video",
        "slot": "Thursday 8:00 AM MDT (Oct 01, 2026)",
        "dueAt": "2026-10-01T14:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "OCTOBER HAS ARRIVED, AND THE BLUE WAVE IS STRONGER THAN EVER 🇨🇼🌊\n\n"
            "New month, same unbreakable spirit.\n\n"
            "Never forget how this squad turned an impossible situation into a national celebration. "
            "Costa Rica 3, Curaçao 4. "
            "Carry that same energy into your business, your sport, and your personal goals this October.\n\n"
            "Ban Kòrsou!\n\n"
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Bring Coach Lornette Daye to your event: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanExcellence #SmallIslandBigDreams #IslandFootball #LornetteDaye"
        )
    },
    {
        "id": 18,
        "type": "video",
        "slot": "Thursday 3:00 PM MDT (Oct 01, 2026)",
        "dueAt": "2026-10-01T21:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "DICK ADVOCAAT'S HALFTIME MASTERCLASS 🇨🇼🧠\n\n"
            "Down 3-0 at the break. What do you say to your players?\n\n"
            "You do not yell; you instruct. You remind them of their quality. "
            "You make clear tactical adjustments. "
            "Advocaat and his staff showed what elite crisis management looks like under a global spotlight.\n\n"
            "Who was your favorite coach that always brought out the best in you? Share your tribute below!\n\n"
            "Dushi Kòrsou!\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Leadership consulting and keynote presentations: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanPride #CaribbeanToTheWorld #SmallIslandBigDreams #CaribbeanPower #LornetteDaye"
        )
    },
    {
        "id": 19,
        "type": "video",
        "slot": "Friday 8:00 AM MDT (Oct 02, 2026)",
        "dueAt": "2026-10-02T14:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "ONE WEEK LATER: THE MATCH THAT CHANGED EVERYTHING 🇨🇼⚽\n\n"
            "Seven days after this historic comeback, the football world is still in awe.\n\n"
            "Four unanswered goals away from home against Costa Rica. "
            "A small Caribbean island demonstrating world-class character. "
            "Every time you rewatch this tape, you see a new example of courage and heart.\n\n"
            "Tag a friend who still needs to see this!\n\n"
            "Ban Kòrsou!\n\n"
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote bookings with Coach Lornette Daye: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #Korsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #LornetteDaye"
        )
    },
    {
        "id": 20,
        "type": "video",
        "slot": "Friday 3:00 PM MDT (Oct 02, 2026)",
        "dueAt": "2026-10-02T21:00:00.000Z",
        "assetFile": "curacao-full-highlights.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Championship Collection ($14.99 CAD) & Speaking",
        "text": (
            "CELEBRATING OUR HERITAGE, OUR TALENT, AND OUR FUTURE 🇨🇼🏆\n\n"
            "This is Curaçao.\n\n"
            "Unshakable, proud, and relentless in pursuit of excellence. "
            "To every player, coach, and supporter who lived through this 4-3 comeback: "
            "thank you for giving us a moment that will live in Caribbean sports folklore forever.\n\n"
            "Keep chasing greatness. Finish strong!\n\n"
            "Ban Kòrsou!\n\n"
            "Explore Coach Lornette Daye's full championship collection ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote and executive coaching inquiries: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanSports #IslandFootball #SmallIslandBigDreams #CaribbeanExcellence #LornetteDaye"
        )
    }
]

def check_for_em_dashes():
    errors = []
    for p in posts_data:
        t = p["text"]
        if "—" in t or "&mdash;" in t or "\u2014" in t:
            errors.append(f"Post {p['id']} contains an em dash!")
    if errors:
        for err in errors:
            print("ERROR:", err)
        sys.exit(1)
    print("EM DASH CHECK: PASS (Zero em dashes found across all 20 posts).")

def schedule_post(post):
    query = '''
    mutation CreatePost($input: CreatePostInput!) {
        createPost(input: $input) {
            __typename
            ... on PostActionSuccess {
                post {
                    id
                    status
                    dueAt
                }
            }
            ... on LimitReachedError {
                message
            }
            ... on InvalidInputError {
                message
            }
            ... on UnexpectedError {
                message
            }
            ... on UnauthorizedError {
                message
            }
        }
    }
    '''

    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": post["text"],
            "schedulingType": "automatic",
            "mode": "customScheduled",
            "dueAt": post["dueAt"],
            "saveToDraft": False,
            "needsApproval": False,
            "assets": [
                {
                    "video": {
                        "url": post["assetUrl"]
                    }
                }
            ]
        }
    }

    data = json.dumps({"query": query, "variables": variables}).encode('utf-8')
    req = urllib.request.Request(
        'https://api.buffer.com',
        data=data,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TOKEN}',
            'User-Agent': 'Mozilla/5.0'
        }
    )

    ctx = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        retry_after = e.headers.get('Retry-After')
        return {
            "error": str(e),
            "status_code": e.code,
            "retry_after": int(retry_after) if retry_after and retry_after.isdigit() else 60
        }
    except Exception as e:
        return {"error": str(e)}

def main():
    print("=" * 75)
    print("STARTING CURAÇAO FULL HIGHLIGHTS CAMPAIGN SCHEDULING (20 POSTS)")
    print("=" * 75)

    check_for_em_dashes()

    report_path = os.path.join(os.path.dirname(__file__), "curacao-full-highlights-scheduled-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    for idx, post in enumerate(posts_data, 1):
        p_id = post["id"]

        if p_id in results and results[p_id].get("postId"):
            print(f"[{idx}/20] Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{idx}/20] Scheduling Post #{p_id} ({post['slot']}) - Due: {post['dueAt']}...")
            print(f"  Asset: {post['assetUrl']}")
            res = schedule_post(post)

            if res.get("status_code") == 429 or "429" in str(res.get("error", "")):
                wait_sec = res.get("retry_after", 60)
                print(f"  [RATE LIMIT] HTTP 429 encountered. Waiting {wait_sec + 5}s...")
                time.sleep(wait_sec + 5)
                continue

            create_post_data = res.get("data", {}).get("createPost", {})
            typename = create_post_data.get("__typename")
            post_obj = create_post_data.get("post")

            if typename == "PostActionSuccess" and post_obj and post_obj.get("id"):
                b_id = post_obj["id"]
                st = post_obj.get("status")
                due = post_obj.get("dueAt")
                print(f"  >>> SUCCESS: Post ID {b_id} scheduled for {due} (status: {st})")
                results[p_id] = {
                    "id": p_id,
                    "type": post["type"],
                    "slot": post["slot"],
                    "dueAt": due,
                    "postId": b_id,
                    "status": st,
                    "assetFile": post["assetFile"],
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"]
                }
                break
            else:
                err_msg = create_post_data.get("message") or res.get("errors") or res.get("error") or str(res)
                print(f"  >>> ERROR: {err_msg}")
                results[p_id] = {
                    "id": p_id,
                    "type": post["type"],
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "assetFile": post["assetFile"],
                    "error": err_msg,
                    "status": "failed"
                }
                break

        time.sleep(2)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 75)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/20 posts scheduled successfully.")

if __name__ == "__main__":
    main()
