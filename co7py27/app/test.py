from systemd import journal

journal.send('Hello world')

print 'test complete'