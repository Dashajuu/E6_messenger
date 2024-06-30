from .models import GroupChat, GroupMessage, PrivateChat, PrivateMessage


def create_group_chat(user, group_name):
    return GroupChat.objects.create(admin=user, name=group_name)


def add_member_to_group(user, group_name):
    group = GroupChat.objects.get(name=group_name)
    return group.members.add(user)


def create_or_add_group(user, group_name):
    group_names = GroupChat.objects.all().values_list('name', flat=True)

    if group_name in group_names:
        add_member_to_group(user, group_name)
    else:
        create_group_chat(user, group_name)
        add_member_to_group(user, group_name)


def create_group_message(user, content, group_name):
    group = GroupChat.objects.get(name=group_name)
    return GroupMessage.objects.create(sender=user, content=content, group=group)


def create_private_message(user, content, chat_id):
    chat = PrivateChat.objects.get(pk=chat_id)
    return PrivateMessage.objects.create(sender=user, content=content, private_chat=chat)
