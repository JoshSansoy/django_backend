from django.db import models
import random

class Monster(models.Model):
    name = models.CharField(max_length=60)
    image = models.URLField(max_length=200)
    description = models.TextField(max_length=132, default = '')
    health = models.IntegerField()
    attack = models.IntegerField()

    def _str_(self):
        return self.name
    
    def doAttack(self):
            attack = self.attack
            critical = ''
            if random.randint(0,100) < 10:
                attack = attack * 2
                critical = 'Critical Hit! '
            text = (critical + self.name + ' attacks for ' + str(attack) + ' damage')
            return [attack, text]

    def takeDamage(self, d=0):
        self.health = self.health - d