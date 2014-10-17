#!/usr/bin/env python

from pushbullet import PushBullet

class pusher:
    def push(self, subject, body):
        pb = PushBullet('stuffhere')
        success, push = pb.push_note(subject, body)
        print success
