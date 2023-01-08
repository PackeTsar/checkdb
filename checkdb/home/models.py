from django.db import models


PROTOCOLS = (
    ('telnet', 'telnet'),
    ('ssh', 'ssh'),
    ('http', 'http'),
    ('http-telnet', 'http-telnet'),
)

ADDRESS_FAMILIES = (
    ('ipv4', 'ipv4'),
    ('ipv6', 'ipv6'),
)


class Record(models.Model):
    timestamp = models.DateTimeField()
    ip = models.CharField(max_length=40)
    address_family = models.CharField(max_length=4, choices=ADDRESS_FAMILIES)
    port = models.PositiveIntegerField()
    protocol = models.CharField(max_length=40, choices=PROTOCOLS)

    def __str__(self) -> str:
        return self.ip
