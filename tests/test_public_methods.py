import unittest

import vcr

from lyricsgenius import PublicAPI

try:
    from .test_genius import test_vcr
except ModuleNotFoundError:
    from test_genius import test_vcr

client = PublicAPI()


class TestAlbumMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up album methods tests...\n")
        cls.album_id = 104614

    @test_vcr.use_cassette
    def test_album(self):
        msg = "Album ID did not match."
        r = client.album(self.album_id)
        self.assertEqual(r['album']['id'], self.album_id, msg)

    @test_vcr.use_cassette
    def test_albums_charts(self):
        msg = "Album charts were empty."
        r = client.albums_charts()
        self.assertTrue("chart_items" in r, msg)

    @test_vcr.use_cassette
    def test_album_comments(self):
        msg = "Album comments were empty."
        r = client.album_comments(self.album_id)
        self.assertTrue("comments" in r, msg)

    @test_vcr.use_cassette
    def test_album_cover_arts(self):
        msg = "Album cover arts were empty."
        r = client.album_cover_arts(self.album_id)
        self.assertTrue("cover_arts" in r, msg)

    @test_vcr.use_cassette
    def test_album_leaderboard(self):
        msg = "Album leaderboard was empty."
        r = client.album_leaderboard(self.album_id)
        self.assertTrue("leaderboard" in r, msg)

    @test_vcr.use_cassette
    def test_album_tracks(self):
        msg = "Album tracks were empty."
        r = client.album_tracks(self.album_id)
        self.assertTrue("tracks" in r, msg)


class TestAnnotationMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up annotation methods tests...\n")
        cls.annotation_id = 10225840

    @test_vcr.use_cassette(
        path_transformer=vcr.VCR.ensure_suffix(' public' + '.' + test_vcr.serializer))
    def test_annotation(self):
        msg = "annotation ID did not match."
        r = client.annotation(self.annotation_id)
        self.assertEqual(r['annotation']['id'], self.annotation_id, msg)

    @test_vcr.use_cassette
    def test_annotation_edits(self):
        msg = "annotation edits were empty."
        r = client.annotation_edits(self.annotation_id)
        self.assertTrue("versions" in r, msg)

    @test_vcr.use_cassette
    def test_annotation_comments(self):
        msg = "annotation comments were empty."
        r = client.annotation_comments(self.annotation_id)
        self.assertTrue("comments" in r, msg)


class TestArticleMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up article methods tests...\n")
        cls.article_id = 11880

    @test_vcr.use_cassette
    def test_article(self):
        msg = "article ID did not match."
        r = client.article(self.article_id)
        self.assertEqual(r['article']['id'], self.article_id, msg)

    @test_vcr.use_cassette
    def test_article_comments(self):
        msg = "article comments were empty."
        r = client.article_comments(self.article_id)
        self.assertTrue("comments" in r, msg)

    @test_vcr.use_cassette
    def test_latest_articles(self):
        msg = "latest articles were empty."
        r = client.latest_articles()
        self.assertTrue("editorial_placements" in r, msg)


class TestArtistMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up artist methods tests...\n")
        cls.artist_id = 1665

    @test_vcr.use_cassette
    def test_artist(self):
        r = client.artist(self.artist_id)
        self.assertEqual(r['artist']['id'], self.artist_id)

    @test_vcr.use_cassette
    def test_artist_activity(self):
        r = client.artist_activity(self.artist_id)
        self.assertTrue("line_items" in r)

    @test_vcr.use_cassette
    def test_artist_albums(self):
        r = client.artist_albums(self.artist_id)
        self.assertTrue("albums" in r)

    # @test_vcr.use_cassette
    # def test_artist_contribution_opportunities(self):
    #     r = client.artist_contribution_opportunities(self.artist_id)
    #     self.assertIsNotNone(r.get('contribution_opportunities'))

    @test_vcr.use_cassette
    def test_artist_followers(self):
        r = client.artist_followers(self.artist_id)
        self.assertTrue("followers" in r)

    @test_vcr.use_cassette
    def test_artist_leaderboard(self):
        r = client.artist_leaderboard(self.artist_id)
        self.assertTrue("leaderboard" in r)

    @test_vcr.use_cassette
    def test_artist_songs(self):
        r = client.artist_songs(self.artist_id)
        self.assertTrue("songs" in r)

    @test_vcr.use_cassette
    def test_search_artist_songs(self):
        r = client.search_artist_songs(self.artist_id, 'test')
        self.assertTrue("songs" in r)


class TestCoverArtMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up cover arts methods tests...\n")
        cls.album_id = 104614

    @test_vcr.use_cassette
    def test_cover_arts(self):
        r = client.cover_arts(self.album_id)
        self.assertTrue("cover_arts" in r)


class TestDiscussionMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up discussion methods tests...\n")
#        cls.discussion_id = 123
#
#    @test_vcr.use_cassette
#    def test_discussion(self):
#        r = client.discussion(self.discussion_id)
#        self.assertEqual(r['discussion']['id'], self.discussion_id)
#
#    @test_vcr.use_cassette
#    def test_discussion_replies(self):
#        r = client.discussion_replies(self.discussion_id)
#        self.assertTrue("forum_posts" in r)

    @test_vcr.use_cassette
    def test_discussions(self):
        r = client.discussions()
        self.assertTrue("discussions" in r)


class TestLeaderboardMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up leaerboard methods tests...\n")

    @test_vcr.use_cassette
    def test_leaderboard(self):
        r = client.leaderboard()
        self.assertTrue("leaderboard" in r)

    @test_vcr.use_cassette
    def test_charts(self):
        r = client.charts()
        self.assertTrue("chart_items" in r)


class TestQuestionMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up question methods tests...\n")
        cls.album_id = 104614

    @test_vcr.use_cassette
    def test_questions(self):
        r = client.questions(self.album_id)
        self.assertIsNotNone(r.get('questions'))


class TestReferentMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up referent methods tests...\n")
        cls.web_page_id = 10347
        cls.referent_ids = [20793764, 20641014]

    @test_vcr.use_cassette
    def test_referent(self):
        r = client.referent(self.referent_ids)
        self.assertTrue(str(self.referent_ids[0]) in r['referents'])
        self.assertTrue(str(self.referent_ids[1]) in r['referents'])

    @test_vcr.use_cassette
    def test_referents(self):
        r = client.referents(web_page_id=self.web_page_id)
        self.assertIsNotNone(r.get('referents'))


class TestSearchMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up search methods tests...\n")
        cls.search_term = 'test'

    @test_vcr.use_cassette
    def test_search(self):
        r = client.search(self.search_term)
        self.assertIsNotNone(r['hits'])

    @test_vcr.use_cassette
    def test_search_albums(self):
        r = client.search_albums(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'album')

    @test_vcr.use_cassette
    def test_search_articles(self):
        r = client.search_articles(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'article')

    @test_vcr.use_cassette
    def test_search_artists(self):
        r = client.search_artists(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'artist')

    @test_vcr.use_cassette
    def test_search_lyrics(self):
        r = client.search_lyrics(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'lyric')

    @test_vcr.use_cassette
    def test_search_songs(self):
        r = client.search_songs(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'song')

    @test_vcr.use_cassette
    def test_search_users(self):
        r = client.search_users(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'user')

    @test_vcr.use_cassette
    def test_search_videos(self):
        r = client.search_videos(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'video')

    @test_vcr.use_cassette
    def test_search_all(self):
        r = client.search_all(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'top_hit')


class TestSongMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up song methods tests...\n")
        cls.song_id = 378195

    @test_vcr.use_cassette
    def test_song(self):
        r = client.song(self.song_id)
        self.assertEqual(r['song']['id'], self.song_id)

    @test_vcr.use_cassette
    def test_song_activity(self):
        r = client.song_activity(self.song_id)
        self.assertTrue("line_items" in r)

    @test_vcr.use_cassette
    def test_song_comments(self):
        r = client.song_comments(self.song_id)
        self.assertTrue("comments" in r)

    @test_vcr.use_cassette
    def test_song_contributors(self):
        r = client.song_contributors(self.song_id)
        self.assertTrue("contributors" in r)


class TestUserMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up user methods tests...\n")
        cls.user_id = 1

    @test_vcr.use_cassette
    def test_user(self):
        r = client.user(self.user_id)
        self.assertEqual(r['user']['id'], self.user_id)

    @test_vcr.use_cassette
    def test_user_accomplishments(self):
        r = client.user_accomplishments(self.user_id)
        self.assertTrue("accomplishments" in r)

    @test_vcr.use_cassette
    def test_user_following(self):
        r = client.user_following(self.user_id)
        self.assertTrue("followed_users" in r)

    @test_vcr.use_cassette
    def test_user_followers(self):
        r = client.user_followers(self.user_id)
        self.assertTrue("followers" in r)

    @test_vcr.use_cassette
    def test_user_contributions(self):
        r = client.user_contributions(self.user_id)
        self.assertTrue("contribution_groups" in r)

    @test_vcr.use_cassette
    def test_user_annotations(self):
        r = client.user_annotations(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'annotation')

    @test_vcr.use_cassette
    def test_user_articles(self):
        r = client.user_articles(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'article')

    @test_vcr.use_cassette
    def test_user_pyongs(self):
        r = client.user_pyongs(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'pyong')

    @test_vcr.use_cassette
    def test_user_questions_and_answers(self):
        r = client.user_questions_and_answers(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'answer')

    @test_vcr.use_cassette
    def test_user_suggestions(self):
        r = client.user_suggestions(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'comment')

    @test_vcr.use_cassette
    def test_user_transcriptions(self):
        r = client.user_transcriptions(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'song')

    @test_vcr.use_cassette
    def test_user_unreviewed(self):
        r = client.user_unreviewed(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'annotation')


class TestVideoMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up video methods tests...\n")
        cls.video_id = 18681

    @test_vcr.use_cassette
    def test_video(self):
        r = client.video(self.video_id)
        self.assertEqual(r['video']['id'], self.video_id)

    @test_vcr.use_cassette
    def test_videos(self):
        r = client.videos(video_id=self.video_id, series=True)
        self.assertTrue("video_lists" in r)

        r = client.videos(video_id=self.video_id)
        self.assertTrue("videos" in r)


class TestMiscMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up misc methods tests...\n")
        # cls.line_item_id = 146262999
        cls.annotation_id = 10225840

    # @test_vcr.use_cassette
    # def test_line_item(self):
    #    r = client.line_item(self.line_item_id)
    #    self.assertTrue("line_item" in r)

    @test_vcr.use_cassette
    def test_voters(self):
        r = client.voters(annotation_id=self.annotation_id)
        self.assertTrue("voters" in r)