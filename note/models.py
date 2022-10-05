# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Admins(models.Model):
#     name = models.CharField(max_length=255)
#     userid = models.CharField(unique=True, max_length=255)
#     password = models.CharField(max_length=255)
#     is_super = models.IntegerField()
#     is_editor = models.IntegerField()
#     phone = models.CharField(max_length=255, blank=True, null=True)
#     remember_token = models.CharField(max_length=100, blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'admins'


# class Articles(models.Model):
#     important = models.IntegerField()
#     type = models.CharField(max_length=255, blank=True, null=True)
#     writer = models.CharField(max_length=255, blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     opened_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'articles'


# class Badges(models.Model):
#     title = models.CharField(max_length=255)
#     code = models.CharField(max_length=255)
#     grade = models.IntegerField()
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     type = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'badges'


# class Bookmarks(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     note = models.ForeignKey('Notes', models.DO_NOTHING)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'bookmarks'


# class Categories(models.Model):
#     category = models.CharField(max_length=255)
#     parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'categories'


# class ChallengeBadge(models.Model):
#     challenge = models.ForeignKey('Challenges', models.DO_NOTHING)
#     badge = models.ForeignKey(Badges, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'challenge_badge'


# class ChallengeRecords(models.Model):
#     challenge = models.ForeignKey('Challenges', models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     param = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'challenge_records'


# class Challenges(models.Model):
#     title = models.CharField(max_length=255)
#     code = models.CharField(max_length=255)
#     type = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     data = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
#     openable = models.IntegerField()
#     started_at = models.DateTimeField(blank=True, null=True)
#     ended_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'challenges'


# class CommercialRecords(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     commercial = models.ForeignKey('Commercials', models.DO_NOTHING, blank=True, null=True)
#     type = models.CharField(max_length=255, blank=True, null=True)
#     data = models.CharField(max_length=255, blank=True, null=True)
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     ipaddr = models.CharField(max_length=255, blank=True, null=True)
#     ua = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'commercial_records'


class Commercials(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    partner = models.CharField(max_length=255)
    commercial_type = models.IntegerField()
    amount = models.PositiveIntegerField()
    prepend_text = models.CharField(max_length=255, blank=True, null=True)
    prepend_text_url = models.CharField(max_length=255, blank=True, null=True)
    main_banner = models.PositiveIntegerField(blank=True, null=True)
    main_banner_mobile = models.PositiveIntegerField(blank=True, null=True)
    main_banner_url = models.CharField(max_length=255, blank=True, null=True)
    ticket_banner = models.PositiveIntegerField(blank=True, null=True)
    ticket_banner_mobile = models.PositiveIntegerField(blank=True, null=True)
    ticket_banner_url = models.CharField(max_length=255, blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    openable = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commercials'


# class Coupons(models.Model):
#     gid = models.CharField(max_length=255)
#     coupon_type = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#     value = models.CharField(max_length=16)
#     code = models.CharField(unique=True, max_length=32)
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     available_days = models.PositiveIntegerField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     ended_at = models.DateTimeField(blank=True, null=True)
#     expired_at = models.DateTimeField(blank=True, null=True)
#     bounded_at = models.DateTimeField(blank=True, null=True)
#     used_at = models.DateTimeField(blank=True, null=True)
#     memo = models.CharField(max_length=255, blank=True, null=True)
#     product_id = models.PositiveIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'coupons'


# class Cps(models.Model):
#     title = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     desc = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'cps'


# class CustomerRequestQuestion(models.Model):
#     customer_request = models.ForeignKey('CustomerRequests', models.DO_NOTHING)
#     question = models.ForeignKey('Questions', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'customer_request_question'


# class CustomerRequests(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255, blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     resolved_at = models.DateTimeField(blank=True, null=True)
#     category = models.TextField()

#     class Meta:
#         managed = False
#         db_table = 'customer_requests'


# class EventRecommenders(models.Model):
#     user_id = models.PositiveIntegerField(blank=True, null=True)
#     recommender_id = models.PositiveIntegerField(blank=True, null=True)
#     payment_id = models.PositiveBigIntegerField(blank=True, null=True)
#     created_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'event_recommenders'


# class FailedJobs(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     uuid = models.CharField(unique=True, max_length=255)
#     connection = models.TextField()
#     queue = models.TextField()
#     payload = models.TextField()
#     exception = models.TextField()
#     failed_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'failed_jobs'


# class FaqQuestion(models.Model):
#     faq = models.ForeignKey('Faqs', models.DO_NOTHING)
#     question = models.ForeignKey('Questions', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'faq_question'


# class Faqs(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     top = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'faqs'


# class Fixtures(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     slug = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     template = models.CharField(max_length=255)
#     content = models.TextField(blank=True, null=True)
#     scripts = models.TextField(blank=True, null=True)
#     styles = models.TextField(blank=True, null=True)
#     opened_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     membership_limit = models.IntegerField()
#     modules = models.CharField(max_length=255, blank=True, null=True)
#     module_options = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'fixtures'


# class Friends(models.Model):
#     title = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     desc = models.TextField(blank=True, null=True)
#     color = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'friends'


# class Images(models.Model):
#     attached_type = models.CharField(max_length=255, blank=True, null=True)
#     attached_id = models.PositiveIntegerField(blank=True, null=True)
#     name = models.CharField(max_length=255)
#     path = models.CharField(max_length=512)
#     flags = models.CharField(max_length=16, blank=True, null=True)
#     copyright = models.CharField(max_length=255, blank=True, null=True)
#     caption = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'images'


# class MembershipNotes(models.Model):
#     membership = models.ForeignKey('Memberships', models.DO_NOTHING)
#     note_id = models.PositiveIntegerField()
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'membership_notes'


# class MembershipUnlimitHistory(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     note_id = models.PositiveIntegerField(blank=True, null=True)
#     used = models.PositiveIntegerField()
#     total = models.PositiveIntegerField()
#     created_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'membership_unlimit_history'


# class Memberships(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
#     sequence = models.PositiveIntegerField()
#     volume = models.PositiveIntegerField()
#     earning_amount = models.PositiveIntegerField()
#     payment = models.ForeignKey('Payments', models.DO_NOTHING, blank=True, null=True)
#     canceled_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     expired_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'memberships'


# class Migrations(models.Model):
#     migration = models.CharField(max_length=255)
#     batch = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'migrations'


# class NoteCategory(models.Model):
#     note = models.ForeignKey('Notes', models.DO_NOTHING)
#     category = models.ForeignKey(Categories, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'note_category'


# class NoteCp(models.Model):
#     note = models.ForeignKey('Notes', models.DO_NOTHING)
#     cp = models.ForeignKey(Cps, models.DO_NOTHING)
#     role = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'note_cp'


# class NoteFriend(models.Model):
#     note = models.ForeignKey('Notes', models.DO_NOTHING)
#     friend = models.ForeignKey(Friends, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'note_friend'


# class NoteProps(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     note = models.ForeignKey('Notes', models.DO_NOTHING)
#     member_count = models.PositiveIntegerField()
#     view_count = models.PositiveIntegerField()
#     progress = models.PositiveIntegerField()
#     kept = models.PositiveIntegerField()
#     completed = models.PositiveIntegerField()
#     rating = models.FloatField()
#     rated1 = models.PositiveIntegerField()
#     rated2 = models.PositiveIntegerField()
#     rated3 = models.PositiveIntegerField()
#     rated4 = models.PositiveIntegerField()
#     rated5 = models.PositiveIntegerField()
#     shotted = models.PositiveIntegerField()
#     stamped = models.PositiveIntegerField()
#     shared = models.PositiveIntegerField()
#     pub_shared_count = models.PositiveIntegerField()
#     user_shared_count = models.PositiveIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'note_props'


# class NoteTag(models.Model):
#     note = models.ForeignKey('Notes', models.DO_NOTHING)
#     tag = models.ForeignKey('Tags', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'note_tag'


class Notes(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    opened_at = models.DateTimeField(blank=True, null=True)
    openable = models.IntegerField()
    is_free = models.IntegerField()
    reveal = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_commercial = models.IntegerField()
    commercial = models.ForeignKey(Commercials, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes'


# class Offlines(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
#     volume = models.PositiveIntegerField()
#     payment = models.ForeignKey('Payments', models.DO_NOTHING, blank=True, null=True)
#     canceled_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'offlines'


# class PasswordResets(models.Model):
#     email = models.CharField(max_length=255)
#     token = models.CharField(max_length=255)
#     created_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'password_resets'


# class Payments(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     muid = models.CharField(unique=True, max_length=255)
#     tuid = models.CharField(max_length=255, blank=True, null=True)
#     paymethod = models.ForeignKey('Paymethods', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
#     coupon = models.ForeignKey(Coupons, models.DO_NOTHING, blank=True, null=True)
#     title = models.CharField(max_length=1000, blank=True, null=True)
#     amount = models.PositiveIntegerField()
#     quantity = models.PositiveIntegerField()
#     ordered_at = models.DateTimeField()
#     scheduled_at = models.DateTimeField(blank=True, null=True)
#     paid_at = models.DateTimeField(blank=True, null=True)
#     failed_at = models.DateTimeField(blank=True, null=True)
#     fail_message = models.CharField(max_length=255, blank=True, null=True)
#     canceled_at = models.DateTimeField(blank=True, null=True)
#     cancel_message = models.CharField(max_length=255, blank=True, null=True)
#     refunded = models.PositiveIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'payments'


# class Paymethods(models.Model):
#     id = models.CharField(primary_key=True, max_length=255)
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     pg = models.CharField(max_length=255)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'paymethods'


# class PrivateCheckouts(models.Model):
#     code = models.CharField(max_length=64)
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     title = models.CharField(max_length=255)
#     amount = models.PositiveIntegerField()
#     description = models.TextField(blank=True, null=True)
#     information = models.TextField(blank=True, null=True)
#     expired_at = models.DateTimeField(blank=True, null=True)
#     muid = models.CharField(unique=True, max_length=255)
#     tuid = models.CharField(max_length=255, blank=True, null=True)
#     paid_at = models.DateTimeField(blank=True, null=True)
#     failed_at = models.DateTimeField(blank=True, null=True)
#     fail_message = models.CharField(max_length=255, blank=True, null=True)
#     canceled_at = models.DateTimeField(blank=True, null=True)
#     cancel_message = models.CharField(max_length=255, blank=True, null=True)
#     refunded = models.PositiveIntegerField()
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'private_checkouts'


# class Products(models.Model):
#     type = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=255, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     information = models.TextField(blank=True, null=True)
#     volume = models.CharField(max_length=255)
#     price = models.CharField(max_length=255)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     public = models.IntegerField()
#     again = models.IntegerField()
#     next_product = models.PositiveIntegerField(blank=True, null=True)
#     bundle_type = models.CharField(max_length=255, blank=True, null=True)
#     bundle_volume = models.CharField(max_length=255, blank=True, null=True)
#     membership_limit = models.IntegerField()
#     quantity_limit = models.IntegerField()
#     opened_at = models.DateTimeField(blank=True, null=True)
#     closed_at = models.DateTimeField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'products'


# class PromotionUsers(models.Model):
#     promotion = models.ForeignKey('Promotions', models.DO_NOTHING)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     data = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
#     registered_at = models.DateTimeField()
#     done_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'promotion_users'


# class Promotions(models.Model):
#     title = models.CharField(max_length=255)
#     type = models.CharField(max_length=255)
#     max = models.PositiveIntegerField()
#     started_at = models.DateTimeField(blank=True, null=True)
#     ended_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     trigger = models.CharField(max_length=255, blank=True, null=True)
#     option = models.CharField(max_length=255, blank=True, null=True)
#     coupon_gid = models.CharField(max_length=255, blank=True, null=True)
#     option_value = models.PositiveIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'promotions'


# class Questions(models.Model):
#     question = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'questions'


# class ShotHistory(models.Model):
#     shot = models.ForeignKey('Shots', models.DO_NOTHING)
#     target_type = models.CharField(max_length=255)
#     target_id = models.PositiveIntegerField(blank=True, null=True)
#     created_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'shot_history'


# class Shots(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
#     used = models.PositiveIntegerField()
#     volume = models.PositiveIntegerField()
#     payment = models.ForeignKey(Payments, models.DO_NOTHING, blank=True, null=True)
#     canceled_at = models.DateTimeField(blank=True, null=True)
#     expired_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'shots'


# class SiteConfigs(models.Model):
#     name = models.CharField(max_length=255)
#     value = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'site_configs'


# class StampRecords(models.Model):
#     stamp = models.ForeignKey('Stamps', models.DO_NOTHING)
#     note = models.ForeignKey(Notes, models.DO_NOTHING)
#     created_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'stamp_records'


# class Stamps(models.Model):
#     sequence = models.PositiveIntegerField()
#     user_id = models.PositiveIntegerField(blank=True, null=True)
#     completed_at = models.DateTimeField(blank=True, null=True)
#     used_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'stamps'


# class Statuses(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     membership = models.ForeignKey(Memberships, models.DO_NOTHING, blank=True, null=True)
#     product_name = models.CharField(max_length=255, blank=True, null=True)
#     product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
#     sequence = models.PositiveIntegerField(blank=True, null=True)
#     paymethod = models.ForeignKey(Paymethods, models.DO_NOTHING, blank=True, null=True)
#     paid_amount = models.PositiveIntegerField(blank=True, null=True)
#     paid_at = models.DateTimeField(blank=True, null=True)
#     started_at = models.DateTimeField(blank=True, null=True)
#     ended_at = models.DateTimeField(blank=True, null=True)
#     joined_at = models.DateTimeField()
#     payment = models.ForeignKey(Payments, models.DO_NOTHING, blank=True, null=True)
#     renewal_payment = models.ForeignKey(Payments, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'statuses'


# class Subscriptions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     pg = models.CharField(max_length=255, blank=True, null=True)
#     cuid = models.CharField(unique=True, max_length=255)
#     card_code = models.CharField(max_length=255, blank=True, null=True)
#     card_name = models.CharField(max_length=255, blank=True, null=True)
#     card_number = models.CharField(max_length=255, blank=True, null=True)
#     card_type = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'subscriptions'


# class Tags(models.Model):
#     tag = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'tags'


# class Terms(models.Model):
#     type = models.CharField(max_length=255)
#     content = models.TextField()
#     opened_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'terms'


# class TicketHistories(models.Model):
#     ticket = models.ForeignKey('Tickets', models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     created_at = models.DateTimeField()
#     continued = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'ticket_histories'


# class TicketJoins(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     ticket_id = models.PositiveIntegerField()
#     email = models.CharField(max_length=255)
#     phonehash = models.CharField(max_length=255, blank=True, null=True)
#     joined_at = models.DateTimeField()
#     done_at = models.DateTimeField(blank=True, null=True)
#     payment = models.ForeignKey(Payments, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ticket_joins'


# class Tickets(models.Model):
#     owner_type = models.CharField(max_length=255, blank=True, null=True)
#     owner_id = models.PositiveIntegerField(blank=True, null=True)
#     note = models.ForeignKey(Notes, models.DO_NOTHING, blank=True, null=True)
#     ticket = models.CharField(max_length=255)
#     created_at = models.DateTimeField()
#     expired_at = models.DateTimeField(blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     promotable = models.IntegerField()
#     freejoinable = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'tickets'


# class UserAuths(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     auth_type = models.CharField(max_length=255)
#     auth_id = models.CharField(max_length=255)
#     join_from = models.IntegerField()
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user_auths'


# class UserBadges(models.Model):
#     badge = models.ForeignKey(Badges, models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     owned_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'user_badges'


# class UserChallenges(models.Model):
#     challenge = models.ForeignKey(Challenges, models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     goaled_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'user_challenges'


# class UserConfigs(models.Model):
#     user_id = models.PositiveIntegerField(blank=True, null=True)
#     name = models.CharField(max_length=255)
#     value = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user_configs'


# class UserInfos(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     addr1 = models.CharField(max_length=2000, blank=True, null=True)
#     addr2 = models.CharField(max_length=2000, blank=True, null=True)
#     postcode = models.CharField(max_length=500, blank=True, null=True)
#     phone = models.CharField(max_length=500, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     name = models.CharField(max_length=500, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user_infos'


# class UserNoteProps(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     note = models.ForeignKey(Notes, models.DO_NOTHING)
#     progress = models.PositiveIntegerField()
#     rating = models.PositiveIntegerField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     scroll = models.PositiveIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user_note_props'


# class UserReport(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     reported_at = models.DateField()
#     user_total = models.PositiveIntegerField()
#     member_total = models.PositiveIntegerField()
#     member_paid = models.PositiveIntegerField()
#     join_total = models.PositiveIntegerField()
#     join_paid = models.PositiveIntegerField()
#     end_today = models.PositiveIntegerField()
#     cancel_today = models.PositiveIntegerField()
#     renewal_today = models.PositiveIntegerField()
#     stopreq_total = models.PositiveIntegerField()
#     stopreq_today = models.PositiveIntegerField()
#     stop_today = models.PositiveIntegerField()
#     shot_today = models.PositiveIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'user_report'


# class Users(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.CharField(unique=True, max_length=255)
#     password = models.CharField(max_length=255)
#     email_verified_at = models.DateTimeField(blank=True, null=True)
#     email_verification_code = models.CharField(max_length=255, blank=True, null=True)
#     terms_agreed_at = models.DateTimeField(blank=True, null=True)
#     privacy_policy_agreed_at = models.DateTimeField(blank=True, null=True)
#     newsletter_subscribed_at = models.DateTimeField(blank=True, null=True)
#     infomail_subscribed_at = models.DateTimeField(blank=True, null=True)
#     remember_token = models.CharField(max_length=100, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     accessed_at = models.DateTimeField(blank=True, null=True)
#     namehash = models.CharField(max_length=255, blank=True, null=True)
#     phonehash = models.CharField(max_length=255, blank=True, null=True)
#     emailhash = models.CharField(max_length=255, blank=True, null=True)
#     pwset_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'users'
