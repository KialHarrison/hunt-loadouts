from django.db import models

MELEE_DAMAGE_TYPES = (
    ('rending', 'Rending'),
    ('blunt', 'Blunt'),
    ('piercing', 'Piercing'),
)

WEAPON_AMMO_TYPES = (
    ('compact', 'Compact'),
    ('medium', 'Medium'),
    ('long', 'Long'),
    ('special', 'Special'),
    ('shotgun', 'Shotgun'),
)

ITEM_TYPES = (
    ('consumable', 'Consumable'),
    ('tool', 'Tool'),
    ('weapon', 'Weapon'),
    ('ammo', 'Ammo'),
)

class Gun(models.Model):
    name = models.CharField(max_length=100)
    damage = models.IntegerField()
    cost = models.IntegerField()
    size = models.IntegerField()
    type = models.CharField(max_length=10, choices=ITEM_TYPES)
    ammo_type = models.CharField(max_length=7, choices=WEAPON_AMMO_TYPES)
    effective_range = models.IntegerField()
    rate_of_fire = models.IntegerField()
    cycle_time = models.IntegerField()
    spread = models.IntegerField()
    sway = models.IntegerField()
    vertical_recoil = models.IntegerField()
    muzzle_velocity = models.IntegerField()
    light_melee_damage = models.IntegerField()
    heavy_melee_damage = models.IntegerField()
    light_melee_stamina = models.IntegerField()
    heavy_melee_stamina = models.IntegerField()
    light_melee_damage_type = models.CharField(max_length=8, choices=MELEE_DAMAGE_TYPES)
    heavy_melee_damage_type = models.CharField(max_length=8, choices=MELEE_DAMAGE_TYPES)
    
    def __str__(self):
        return self.name
    
class Loadout(models.Model):
    name = models.CharField(max_length=30, unique=True)
    weapon_one = models.ForeignKey(Gun, on_delete=models.CASCADE, related_name='loadout_weapon_one')
    weapon_two = models.ForeignKey(Gun, on_delete=models.CASCADE, related_name='loadout_weapon_two')
    description = models.TextField()

    def __str__(self):
        return self.name

    