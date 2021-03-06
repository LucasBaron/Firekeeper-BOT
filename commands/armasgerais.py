from discord.ext import commands
from discord.ext.commands import bot
import discord

class Armas(commands.Cog):
    
      def __init__(self, bot):
            self.bot = bot
            print("FOI", self.bot)


      @commands.command(name="teste")
      async def teste(self, ctx):
            name = ctx.author.name

            response = "teste foi"

            await ctx.send(response)
      @commands.command(name="armas")
      async def armas(self, ctx):
            url_image=""
            

            embed = discord.Embed(
                  title="Todas as Armas",
                  description="Armas Disponiveis: ",
                  color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Machados (M)", value = "Battle Axe \ Beast Cutter   \   Brigand Axe  \  Butcher Knife  \  Demon's Axe  \  Dragonslayer's Axe  \  Eleonora  \  Gargoyle Tail Axe  \  Guillotine Axe  \  Hand Axe  \  Millwood Battle Axe  \  Red Rust Sword  \  Serpentine Axe  \  Serpentine Hatchet  \  Thrall Axe"),
            embed.add_field(name="Arcos (A)", value = "Black Bow of Pharis \ Composite Bow \ Darkmoon Longbow \ Dragonrider Bow \ Flynn's Bow \ Longbow \ Scholar's Bow \ Short Bow \ White Birch Bow"),
            embed.add_field(name="Battlestaves (B)", value = "Archdeacon's Longstaff \ Corvian Longstaff \ Heretic's Warstaff \ King's Quarterstaff \ Longstaff of Rosaria \ Murky Warstaff \ Phosphorescent Pole \ Staff of Serpents \ Witch's Staff \ Witchtree Limb"),
            embed.add_field(name="Garras (G)", value = "Beast Claw \ Claw \ Crab Claw \ Crow Talons \ Manikin Claws"),
            embed.add_field(name="Crossbows (CB)", value = "Arbalest \ Avelyn \ Birch Crossbow \ Knight's Crossbow \ Oak Crossbow \ Repeating Crossbow \ Sniper Crossbow"),
            embed.add_field(name="Espadas Curvas (EC)", value = "Beasthunter Saif \ Blind \ Burial Blade \ Carthus Curved Sword \ Carthus Shotel \ Crescent Moon Sword \ Falchion \ Follower Sabre \ Machete \ Painting Guardian's Curved Sword \ Pontiff Knight Curved Sword \ Quelaag's Fury Sword \ Rotten Ghru Curved Sword \ Scimitar \ Shotel \ Smouldering Curved Sword \ Storm Curved Sword \ Worker Machete"),
            embed.add_field(name="Espadas Curvas Grandes (ECG) ", value = "Carthus Curved Greatsword \ Exile Greatsword \ Gravelord Sword \ Harald Curved Greatsword \ Murakumo \ Old Wolf Curved Sword \ Pontiff Knight Greatsword \ Server"),
            embed.add_field(name="Adagas (A)", value = "Aquamarine Dagger \Bandit's Knife \ Corvian Greatknife \ Dagger \ Engraved Dagger \ Firelink Dagger \ Frostfall \ Handmaid's Dagger \ Harpe \ Kris Blade \ Mail Breaker \ Murky Hand Scythe \ Needle of Eternal Agony \ Parrying Dagger \ Rotten Ghru Dagger \ Sage's Stiletto \ Scholar's Candlestick \ Shiv \ Smouldering Dagger \ Tailbone Short Sword \ Thrall Harpe"),
            embed.add_field(name="Soqueiras/Punhos (S)", value = "Caestus \ Censuring Palm \ Dark Hand \ Demon's Fist \ Dragon Bone Fist \ Drake Fist \ Fists \ Hands of God \ Hands of Sin"),
            embed.add_field(name="Martelos Grandes (MTG)", value = "Ash Demon Hammer \ Bloodletter \ Bramd \ Church Pick \ Demon's Great Hammer \ Dragon Hunter's Great Hammer \ Dragon Hunter's Warpick \ Dragon Tooth \ Elder Ghru Tree \ Gargoyle Flame Hammer \ Giant Crab Arm \ Grant \ Great Club \ Great Mace \ Great Wooden Hammer \ Greatwood Club \ Kirkhammer \ Large Club \ Ledo's Great Hammer \ Locust Arm \ Morne's Great Hammer \ Old King's Great Hammer \ Pickaxe \ Quakestone Hammer \ Sacred Chime Hammer \ Sanctum Mace \ Smelter Hammer \ Smough's Great Hammer \ Spiked Mace \ Vordt's Great Hammer"),
            embed.add_field(name="Machados Grandes (MCG)", value = "Black Dragon Greataxe \ Black Knight Greataxe \ Demon King's Greataxe \ Demon's Great Axe \ Dozer Axe \ Dragon Hunter's Greataxe \ Dragon King Greataxe \ Dragonslayer Greataxe \ Earth Seeker \ Golem Axe \ Great Machete \ Greataxe \ Old Knight Battle Axe \ Serpentine Battle Axe \ Yhorm's Great Machete"),
            embed.add_field(name="Arcos Grandes (AG)", value = "Dragonslayer Greatbow \ Millwood Greatbow \ Onislayer Greatbow"),
            
            
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="armas2")
      async def armas2(self ,ctx):
            url_image=""
      

            embed = discord.Embed(
                  title="Todas as Armas",
                  description="Armas Disponiveis: ",
                  color = 0xFFFFFF  
            )
            embed.set_author(name= self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)
            
            embed.add_field(name="Espadas Grandes (EG)", value = "Bastard Sword \ Black Dragon Greatsword \ Black Knight Sword \ Claymore \ Drakeblood Greatsword \ Executioner's Greatsword \ Firelink Greatsword \ Flamberge \ Gael's Greatsword \ Great Lord Greatsword \ Greatsword of Artorias \ Greatsword of Judgment \ Hallowed Greatsword \ Hollowslayer Greatsword \ Irithyll Greatsword \ Key to the Embedded \ Man Serpent Greatsword \ Moonlight Greatsword \ Morion Great Blade \ Obsidian Greatsword \ Onyx Blade \ Spiral Greatsword \ Stone Greatsword \ Storm Ruler \ Sunlight Greatsword \ Sword of Avowal \ Thorned Greatsword \ Twin Princes' Greatsword \ Wolf Knight's Greatsword \ Wolnir's Holy Sword"),
            embed.add_field(name="Alabardas (AL)", value = "Ancient Dragon Halberd \ Bardiche \ Black Knight Glaive \ Crescent Axe \ Crucifix of the Mad King \ Dragonrider Halberd \ Gargoyle Halberd \ Giant's Halberd \ Gundyr's Halberd \ Halberd \ Helix Halberd \ Hunter Axe \ Lucerne \ Old Knight Glaive \ Red Hilted Halberd \ Splitleaf Glaive \ Winged Knight Halberd"),
            embed.add_field(name="Martelos (M)", value = "Aldia Hammer \ Blacksmith Hammer \ Boom Hammer \ Club \ Frying Pan \ Hammer of the Great Tree \ Handmaid's Ladle \ Irithyll Mace \ Irithyll Warpick \ Mace \ Morning Star \ Reinforced Club \ Sanguinus \ Tailbone Club \ Thrall Pick \ Tonitrus \ Warpick \ Wooden Mallet \ Writhing Hammer"),
            embed.add_field(name="Katanas (K)", value = "Bewitched Alonne Sword \ Black Blade \ Bloodlust \ Chaos Blade \ Darkdrift \ Frayed Blade \ Makoto \ Rakuyo \ Uchigatana \ Washing Pole"),
            embed.add_field(name="Lan??as Grandes (LG)", value = "Chariot Lance \ Grand Lance \ Heide Greatlance \ Heide Lance \ Irithyll Lance \ Rampart Golem Lance"),
            embed.add_field(name="Piques (P)", value = "Hunter's Log \ Lothric Knight Long Spear \ Lothric War Banner \ Moonlight Butterfly Horn \ Pike \ Ringed Knight Spear \ Titanite Catch Pole"),
            embed.add_field(name="Foices (F)", value = "Bone Scythe \ Burial Scythe \ Friede's Great Scythe \ Great Corvian Scythe \ Great Scythe \ Lothric's Scythe \ Pontiff Knight Great Scythe \ Priscilla's Scythe \ Scythe of Nahr Alma \ Scythe of Want"),
            embed.add_field(name="Sidearms (S)", value = "Cannon \ Church Cannon \ Evelynn \ Fist of Gratia \ Hunter's Blunderbuss \ Hunter's Pistol \ Repeating Pistol \ Rosamarinus"),
            embed.add_field(name="Lan??as (L)", value = "Arstor's Spear \ Branding Iron \ Channeler's Trident \ Demon's Spear \ Dragonslayer Spear \ Dragonslayer Swordspear \ Firelink Spear \ Follower Javelin \ Four-pronged Plow \ Gargoyle Bident \ Gargoyle Flame Spear \ Istarelle \ Partizan \ Rotten Ghru Spear \ Saint Bident \ Scraping Spear \ Silver Knight Spear \ Smouldering Spear \ Spear \ Spitfire Spear \ Tailbone Spear \ Winged Spear \ Yorshka's Spear"),
            embed.add_field(name="Espadas Retas (ER)", value = "Anri's Straight Sword \ Astora Straight Sword \ Balder Side Sword \ Barbed Straight Sword \ Black Dragon Sword \ Blueblood Sword \ Broadsword \ Broken Straight Sword \ Crystal Straight Sword \ Dark Sword \ Drake Sword \ Firelink Sword \ Hallowed Sword \ Irithyll Straight Sword \ Long Sword \ Lothric Knight Sword \ Lothric's Holy Sword \ Moonlight Sword \ Morion Blade \ Penetrating Sword \ Ringed Knight Straight Sword \ Shortsword \ Silver Knight Straight Sword \ Smouldering Blade \ Sunlight Straight Sword"),
            embed.add_field(name="Rapieiras (R)", value = "Black Scorpion Stinger \ Bone Rapier \ Crystal Sage's Rapier \ Estoc \ Firelink Rapier \ Irithyll Rapier \ Rapier \ Ricard's Rapier \ Velka's Rapier"),
            embed.add_field(name="Ultra Greatswords (UG)", value = "Abyssal Blade \ Abyssal Greatsword \ Astora Greatsword \ Black Knight Greatsword \ Cathedral Knight Greatsword \ Crypt Blacksword \ Demon's Machete \ Dragon Bone Smasher \ Dragon Greatsword \ Drakewing Ultra Greatsword \ Fume Ultra Greatsword \ Greatsword \ Ivory King Ultra Greatsword \ King's Ultra Greatsword \ Lorian's Greatsword \ Lothric Knight Greatsword \ Marvelous Zweihander \ Meat Cleaver \ Profaned Greatsword \ Pursuer's Ultra Greatsword \ Smelter Sword \ Zweihander"),
            embed.add_field(name="Chicotes (C)", value = "Notched Whip \ Serpentine Chain-axe \ Spotted Whip \ Whip \ Witch's Locks"),
            embed.add_field(name="Armas Duplas (AD)", value = "Blades of Mercy \ Brigand Twindaggers \ Chikage \ Ciaran's Tracers \ Crow Quills \ Dancer's Enchanted Swords \ Drang Hammers \ Drang Twinspears \ Farron Greatsword \ Fume Slated Swords \ Giant Door Shield \ Gotthard Twinswords \ Imperious Greatshield \ Melu Scimitars \ Missionary Axes \ Nil Bow and Blade \ Old Knight Maces \ Onikiri and Ubadachi \ Ringed Knight Paired Greatswords \ Runelock \ Sellsword Twinblades \ Serpentine Twindaggers \ Twinspears of the Forlorn \ Valorheart \ Warden Twinblades \ Winged Knight Twinaxes"),

            embed.set_image(url=url_image)
            await ctx.send(embed=embed)
      @commands.command(name="arma_AD_RKPG")
      async def AD_RKPG(self, ctx):
            url_image="https://media.discordapp.net/attachments/925612211479642212/925621244798304366/unknown.png"
      

            embed = discord.Embed(
            title="Ringed Knight Paired Greatswords",
            description="A absor????o da guarda desta arma aumenta com a destreza e a estabilidade com a for??a. A apar??ncia desta arma ?? afetada pela infus??o de Fogo. ",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Brasa: Cruze as duas grandes espadas gastas pelo tempo para reacender uma chama de curta dura????o. Um movimento para cima r??pido como um rel??mpago corta o pr??prio ar e faz a transi????o para ataques normais ou fortes.", value="Dropado pelo Ringed Knight em frente ao altar da Covenant Spears of the Church em The Ringed City")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:ringed-knight-paired-greatswords/ringed_knight_paired_greatswords.PNG")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_BA")
      async def M_BA(self, ctx):
            url_image="https://media.discordapp.net/attachments/922892242249740369/925975243313545316/unknown.png"
      

            embed = discord.Embed(
            title="Battle Axe",
            description="Machado facilmente manejado para batalha e infligindo dano padr??o. Seu peso pode ser usado para infligir altos danos, mas deve ser usado com cuidado, pois deixa seu portador vulner??vel a retalia????o.  ",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Grito de Guerra :Solte um grito de guerra animado que aumenta temporariamente o ataque em 15% por 20 segundos.", value="Vendido pelo ferreiro Andre por 1.000 almas Ou Arma inicial da classe Warrior.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:battle-axe/Battle-Axe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_BC")
      async def M_BC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/925980416840704110/unknown.png"
      

            embed = discord.Embed(
            title="Beast Cutter",
            description="Um cutelo de ferro grosso usado para cortar as peles de feras mais resistentes. Usado pelos trabalhadores da Col??nia de Mortos-Vivos para afastar feras. Efeito: substitui esquiva por Hunter Dash se habilitado em Benjin. Desativado se a carga atual do equipamento estiver acima de 70% do m??x.  ",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash :Divida em inimigos com um grande movimento girat??rio e continue girando para fazer a transi????o para um ataque forte.", value="Equipamento inicial da classe Collector. Encontrado em um ba?? Trancado no assentamento de mortos-vivos.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:beast-cutter/beast-cutter.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_BRA")
      async def M_BRA(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926162513404497981/unknown.png"
      

            embed = discord.Embed(
            title="Brigand Axe",
            description="Machado preferido por bandidos de uma terra distante. Machado de batalha surpreendentemente robusto que requer mais for??a para manejar do que um machado padr??o.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Grito de Guerra :Solte um grito de guerra animado que aumenta temporariamente o ataque em 15% por 20 segundos.", value="Vendido pelo Blacksmith Andre por 2.000 Souls depois de derrotar a Curse-rotted Greatwood. ou Encontrado na Estrada dos Sacrif??cios.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:brigand-axe/Brigand-Axe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_BK")
      async def M_BK(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926170274066489384/unknown.png"
      

            embed = discord.Embed(
            title="Bucher Knife",
            description="Faca de a??ougueiro com uma l??mina estranhamente grande empunhada pela louca que assombra a Estrada dos Sacrif??cios. Ataques obtidos com precis??o restauram o HP. A quantidade varia com o ataque usado. De volta ao Undead Settlement, a mulher adquiriu o gosto pela carne humana, da qual ela se alegrou em participar.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Agu??ar: Afiar a l??mina aumenta o HP restaurado a cada golpe bem-sucedido. Ataques leves / correr / rolar / mergulhar curam 1 + 0,1% de HP ao acertar. \ Ataque pesado sem carga cura (1 + 0,1%) + (3 + 0,5%) HP ao acertar. \ O ataque pesado carregado cura (1 + 0,1%) + (7 + 1%) HP ao acertar. \ A cura ?? a mesma para ataques com uma e duas m??os. \ Stacka a cura com sua pr??pria arte de arma e a infus??o Dark.", value="Deixado por Isabella, a Louca, ao lado do Anel Blight encontrado na ravina na ??rea entre a fogueira da Estrada dos Sacrif??cios e a fogueira da Fortaleza de Meio Caminho.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:butcher-knife/Butcher-Knife.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_DGA")
      async def M_DGA(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926191677574623242/unknown.png"
      

            embed = discord.Embed(
            title="Dragonslayer's Axe",
            description="Machado preferido por Creighton, o Andarilho, infame desertor dos Cavaleiros de Mirrah. Chamado de Machado de Matador de Drag??es pelo rel??mpago que pulsa dentro de sua l??mina, mas Creighton o usou para matar homens.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Grito de Guerra :Solte um grito de guerra animado que aumenta temporariamente o ataque em 15% por 20 segundos.", value="Transposi????o dos dedos de Rosaria em troca de 10 Pale Tongue e 16.000 Souls \ Da fogueira da Igreja de Yorshka em Irithyll do Vale Boreal, siga em dire????o ?? ??rea do cemit??rio ?? esquerda. A partir daqui v?? em dire????o a uma ??rvore que cont??m um item, aderindo ?? direita. Certifique-se de estar no modo Lord of Cinder usando uma brasa. Voc?? ser?? invadido por Creighton the Wanderer e ele deixar?? cair a arma. Voc?? n??o pode ser invadido se tiver derrotado o Pont??fice Sulyvahn.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:dragonslayer-s-axe/Dragonslayer-s-Axe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_DA")
      async def M_DA(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926184245544775720/unknown.png"
      

            embed = discord.Embed(
            title="Demon's Axe",
            description="Este machado, um favorito entre os dem??nios, cont??m a for??a do fogo. Os dem??nios, nascidos do Caos, abrigam fogo, e ainda assim s??o retorcidos e malformados, de forma que nunca foram feitos para existir.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Demonic Flare: Fa??a com que a chama dentro de si se acenda e esmague-a na terra e nos inimigos. Imbui a arma com fogo, adicionando 100 de dano de fogo por 60 segundos.", value="Dropado by Chaos Servant Eygor.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:demon-s-axe/Demon-s-Axe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_E")
      async def M_E(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926197097953378355/unknown.png"
      

            embed = discord.Embed(
            title="Eleonora",
            description="Uma estranha arma encontrada entre os habitantes malformados da Capital Profanada. A Chama Profanada foi desencadeada pela maldi????o dessas mulheres, parentes de um determinado or??culo, mas apesar de sua culpabilidade, seguiram vivendo, sem nenhum cuidado.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Feast Bell: Segure o machado e acene para emitir um carrilh??o solene para adicionar temporariamente 50 sangramento infligido e para restaurar 1% + 10 HP para cada acerto.", value="Dropado pela Monstrosity of Sin encontrada no p??ntano t??xico da Capital Profanada.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:eleonora/Eleonora.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_GTA")
      async def M_GTA(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926199155649548288/unknown.png"
      

            embed = discord.Embed(
            title="Gargoyle Tail Axe",
            description="Cauda cortada das g??rgulas de sino que outrora protegiam um sino acima de uma igreja morta-viva. Ou talvez???? Uma r??plica dif??cil de distinguir da arma real. Exceto que n??o se dobra de forma alguma durante ataques pesados, mostrando sua natureza como uma imita????o.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Burning Slash: Defina a arma acesa, aumentando o ataque de fogo em 80 por 10 segundos, e corte os inimigos com um grande movimento girat??rio, e siga com um forte ataque para um golpe girat??rio vertical.", value="Transposi????o da Chaos Servants em troca de 15 Fire Seeds e 46.000 Almas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:gargoyle-tail-axe/Gargoyle-Tail-Axe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_GA")
      async def M_GA(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926202258436288582/unknown.png"
      

            embed = discord.Embed(
            title="Guillotine Axe",
            description="Um machado que ?? usado para decapita????es que est?? muito desgastado. Tem cabo gorduroso, ?? curto e pesado, mas pode cortar a v??rtebra cervical com um ??nico golpe. ?? desprezado como arma de decapita????o.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Corte vigoroso: Lance em seu inimigo um ataque forte que perfura os escudos, depois prossiga com um ataque forte para um golpe profundo.", value="Encontrado no Mundo Pintado de Ariandel.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:guillotine-axe/guillotine-axe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_HA")
      async def M_HA(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926206422201540678/unknown.png"
      

            embed = discord.Embed(
            title="Hand Axe",
            description="Um rude machado de m??o que serve tanto como arma quanto como ferramenta de muitos usos. Favorecido pelos piromantes do Grande P??ntano, este machado tem um alcance curto, mas apenas peso moderado e dano razo??vel. Facilmente manejado e mais poderoso do que parece.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Grito de Guerra :Solte um grito de guerra animado que aumenta temporariamente o ataque em 15% por 20 segundos.", value="Vendido pelo ferreiro Andre por 800 almas. Arma inicial da classe Pyromancer.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:hand-axe/Hand-Axe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_MBA")
      async def M_MBA(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926251606314450974/unknown.png"
      

            embed = discord.Embed(
            title="Millwood Battle Axe",
            description="Machado de batalha empunhado por Millwood Knights. Sua l??mina ?? aben??oada pelo s??mbolo do Carvalho Et??reo. Um machado robusto normalmente empunhado pelo mais poderoso dos guerreiros.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Grito De Guerra: O grito de guerra ??nico dos Cavaleiros de Millwood envolveu um salto direto para o inimigo e um rugido assustador.", value="Dropado por um Cavaleiro Millwood encontrado no Mundo Pintado de Ariandel.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:millwood-battle-axe/Millwood-Battle-Axe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_RRS")
      async def M_RRS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926252567003004958/unknown.png"
      

            embed = discord.Embed(
            title="Red Rust Sword",
            description="Espada reta do guerreiro Vengarl de Forossa. Esta espada est?? desgastada pela batalha e terrivelmente enferrujada, mas continua sendo uma arma mortal devido ao seu peso incr??vel. Diz a lenda que foi constru??do para testar os limites da for??a dos cavaleiros de Forossa, at?? que Vengarl o balan??ou como um brinquedo de madeira, reivindicando a posse por demonstra????o.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Forossan Warcry: Solte um grito de guerra animado que aumenta temporariamente o ataque em 15% por 20 segundos e permite um ataque forte e esmagador.", value="Transposi????o da Servant of the Rat  em troca de 15 Rat Tail e 38.000 Almas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:red-rust-sword/Red-Rust-Sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_SA")
      async def M_SA(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926254520462348318/unknown.png"
      

            embed = discord.Embed(
            title="Serpentine Axe",
            description="Machado de duas pontas empunhado pelos homens-serpente do pico do Archdragon. Muitos perseguiram o poder dos drag??es ao longo dos tempos, mas nenhum conseguiu replicar sua gl??ria ??nica",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Grito de Guerra :Solte um grito de guerra animado que aumenta temporariamente o ataque em 15% por 20 segundos.", value="Dropado por um m??mico no Pico do Archdragon.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:serp-axe/serp-axe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_SH")
      async def M_SH(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926266386844639313/unknown.png"
      

            embed = discord.Embed(
            title="Serpentine Hachet",
            description="Machado dos homens serpentes que guardam o Pico do Arqudrag??o. Possui uma l??mina ??nica e amplamente curva que pode passar furtivamente pelos escudos.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Stomp: Use seu peso para avan??ar com uma postura baixa e equil??brio aumentado, e siga com um ataque forte e esmagador que perfura escudos para infligir dano direto.", value="Vendido pelo Blacksmith Andre por 6.000 Souls ap??s derrotar The Nameless King. Dropado por um m??mico no pico do Archdragon.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:serpentine-hatchet/Serpentine-Hatchet.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_M_TA")
      async def M_TA(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926283721785638922/unknown.png"
      

            embed = discord.Embed(
            title="Thrall Axe",
            description="Pequeno machado de m??o usado pelos escravos Lothric. Uma arma astuta para um lote astuto, este machado ?? r??pido e mortal. A apar??ncia desta arma ?? afetada pela infus??o de Fogo.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Quickstep de habilidade: Imediatamente fique atr??s ou ao lado dos inimigos. Especialmente eficaz quando travado no alvo.", value="Vendido pelo ferreiro Andre por 5.000 almas ap??s derrotar a Curse-rotted Greatwood ou Encontrado no assentamento de mortos-vivos")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:thrall-axe/Thrall-Axe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_B_AL")
      async def B_AL(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926323250613600267/unknown.png"
      

            embed = discord.Embed(
            title="Archdeacon's Longstaff",
            description="O bast??o de batalha j?? foi usado pelos arquidi??conos da Catedral das Profundezas. Ap??s a morte de um inimigo, cad??veres pr??ximos explodem com energias sombrias.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Gambito do Arquidi??cono: Bata o bast??o no ch??o para despert??-lo brevemente, em seguida, siga com um forte ataque para provocar um rugido, uma b??n????o ou irrita????o.", value="Transposi????o da Aldrich Faithful em troca de 10 Human Dregs e 15.000 almas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:archdeacon-s-longstaff/archdeacon-s-longstaff.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)                 
      @commands.command(name="arma_B_CL")
      async def B_CL(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926323250613600267/unknown.png"
      

            embed = discord.Embed(
            title="Corvian Longstaff",
            description="A batalha de um contador de hist??rias corviano. Manchado pela lama nociva encontrada na Fortaleza Farron. A apar??ncia e o efeito da nuvem nociva s??o afetados pelas infus??es de Sangue, Maldi????o e Gelo.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Poison Spores: Expele esporos nocivos das coisas sem forma e parasitas que habitam o cajado.", value="Vendido pelo Blacksmith Andre por 4.000 Souls ap??s derrotar os Abyss Watchers. Encontrado na Estrada dos Sacrif??cios.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:corvian-longstaff/Corvian-Longstaff.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_B_HW")
      async def B_HW(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926524258006491206/unknown.png"
      

            embed = discord.Embed(
            title="Heretic's Warstaff",
            description="Uma Battlestaff de batalha frequentemente usada por feiticeiros hereges que viajam pela Fortaleza Farron.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Wretch Earth: Empurre o bast??o para a terra para desencadear tremores explosivos.", value="Vendido pelo Blacksmith Andre por 8.000 Souls ap??s derrotar os Abyss Watchers. Peregrinos da transposi????o das Trevas em troca de 3 Fragmentos Abissais e 4.000 Almas ou Encontrado em Farron Keep.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:heretic-s-warstaff/Heretic-s-Warstaff.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_B_KQ")
      async def KQ(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926526654464012288/unknown.png"
      

            embed = discord.Embed(
            title="King's Quarterstaff",
            description="Quarterstaff escavado de uma ??rvore sagrada de Lindelt por um senhor sem nome que passava. Quando com as duas m??os, o portador pode variar seus golpes com ataques exclusivos com a m??o esquerda. Efeito: Ataques sucessivos geram uma corrente el??trica.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Fluxo Elemental da Habilidade: Levante o bast??o no ar para invocar a ira do criador da arma, permitindo ataques especiais fortes.", value="Firelink Shrine - Transposto da Alma do Rei Sem Nome.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:king-s-quarterstaff/king-s-quarterstaff.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_B_LR")
      async def B_LR(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926595408669605919/unknown.png"
      

            embed = discord.Embed(
            title="Longstaff of Rosaria",
            description="A espada de batalha de Rosaria, usada por ela seguidores devotados. Efeito: aumenta a descoberta de itens em 25. Usar a infus??o Lucky nesta arma aumentar?? seu b??nus de descoberta de item para +50. Considerada uma arma da sorte.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="B??n????o de habilidade de Rosaria: Balance o cajado bem alto para receber a b??n????o de Rosaria, aumentando em 30 a Sorte para si e para os que est??o nas proximidades.", value="Firelink Shrine - Transposto da Alma de Rosaria.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:longstaff-of-rosaria/Longstaff-of-Rosaria.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_B_MW")
      async def B_MW(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926596773424812164/unknown.png"
      

            embed = discord.Embed(
            title="Murky Warstaff",
            description="Uma espada de batalha tenebrosa usada pelos habitantes do p??ntano.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade de golpes concussivos: Execute ataques consecutivos implac??veis ???enquanto tra??a um c??rculo.", value="Dropado por um m??mico encontrado na Catedral das Profundezas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:murky-warstaff/murky_warstaff.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_B_PP")
      async def B_PP(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/926603611859988480/unknown.png"
      

            embed = discord.Embed(
            title="Phosphorescent Pole",
            description="Um longo bast??o incrustado com uma joia prism??tica, mantida leve por meio de magia latente. Uma vez pertencente a uma bruxa no c??u, Lorde Rydyell em uma de suas fa??anhas mais famosas roubou-o dela. Apesar de todo o seu brilho, no entanto, ele nunca poderia desbloquear seu verdadeiro poder, a bruxa havia muito tempo selado ap??s consider??-lo muito perigoso. O tempo, entretanto, desgasta todas as coisas, at?? mesmo o selo da Bruxa ... Efeito: a magia latente destr??i as defesas inimigas, reduzindo todas as absor????es em 2% por acerto. Dura 10 segundos, acumula.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Phosphorescent Madness: Eleve o cajado ao c??u para liberar a magia primitiva selada profundamente, levando o portador temporariamente ?? loucura, permitindo rajadas de ataques pesados ??????e selvagens e aumentando o dano F??sico, M??gico, Fogo, Rel??mpago e Escuro em 20 por 30 segundos.", value="Dropado por um m??mico encontrado em Assentamento dos mortos-vivos.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:phosphorescent-pole/phosphorescent-pole.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_B_SS")
      async def B_SS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927043300450533416/unknown.png"
      

            embed = discord.Embed(
            title="Staff of Serpents",
            description="A battlestaff dos homens-serpentes que habitam o pico do Archdragon. Arremessa uma lan??a rel??mpago com ataques carregados com uma m??o.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade de expulsar rel??mpagos: Carregue com o cajado na cintura para envolv??-lo com rel??mpagos, adicionando 60 de dano de Raio por 60 segundos e, em seguida, libere os relampagos com o golpe final.", value="Dropado por Dragon Cultist ou Equipamento inicial da classe Monk.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:staff-of-serpents/staff-of-serpents.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_B_WS")
      async def B_WS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927045554775658506/unknown.png"
      

            embed = discord.Embed(
            title="Witch's Staff",
            description="Uma das batalhas usadas em Izalith antes de sua destrui????o. Efeito: aumenta a Attunement em 5.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Vomitar Fogo: Ancorar o bast??o e usar um forte ataque para cuspir fogo com a ponta do bast??o.", value="Encontrado em um ba?? preso em Smouldering Lake.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:witch-s-staff/Witch-s-Staff.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)                         
      @commands.command(name="arma_B_WL")
      async def B_WL(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927204172909117450/unknown.png"
      

            embed = discord.Embed(
            title="Witchtree Limb",
            description="O membro de uma ??rvore de bruxa. Rude, mas eficaz. A absor????o da guarda desta arma aumenta com a destreza e a estabilidade com a for??a.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Limb Sweep: Varra os inimigos em um grande movimento girat??rio e utilize o momentum para fazer a transi????o para um golpe de ataque forte com as m??os.", value="Dropado por um m??mico encontrado em Irithyll of the Boreal Valley.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:witchtree-limb/Witchtree-limb.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_BBP")
      async def A_BBP(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927290409078628402/unknown.png"
      

            embed = discord.Embed(
            title="Black Bow of Pharis",
            description="Um arco longo preto com o nome de um antigo her??i. Conhecido pela postura incomum com que ?? disparado. Tem um alcance maior do que os arcos padr??o, mas o uso bem-sucedido requer uma m??o treinada e h??bil.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Pharis Triple-shot: Rapidamente arma tr??s flechas com sutileza depois de puxar o arco, disparando-as simultaneamente.", value="Dropado por um do grupo de tr??s Elder Ghrus em Farron Keep.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:black-bow-of-pharis/Black-Bow-of-Pharis.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_CB")
      async def A_CB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927293775884189726/unknown.png"
      

            embed = discord.Embed(
            title="Composite Bow",
            description="Arco curto composto enfatizando o poder. Seu tamanho permite fotos r??pidas. Embora mais poderoso do que arcos padr??o, tamb??m requer mais for??a do usu??rio e seu alcance ?? curto.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Rapid Fire: Rapidamente posiciona as flechas com sutileza ap??s puxar o arco, permitindo tiros consecutivos.", value="Vendido pelo Blacksmith Andre por 3.500 Souls ap??s derrotar os Abyss Watchers. Equipamento inicial da classe Hunter.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:composite-bow/Composite-Bow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_DL")
      async def A_DL(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927295185111625848/unknown.png"
      

            embed = discord.Embed(
            title="Darkmoon Longbow",
            description="Longbow de Darkmoon Gwyndolin, que foi gradualmente devorado por Aldrich. Este arco dourado est?? imbu??do de magia poderosa e ?? mais impressionante com as setas do luar.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Darkmoon Arrow: Libere uma flecha m??gica poderosa, perfurando todos os inimigos em seu caminho.", value="Firelink Shrine - Transposto da Alma de Aldrich.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:darkmoon-longbow/Darkmoon-Longbow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_DB")
      async def A_DB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927299110942429184/unknown.png"
      

            embed = discord.Embed(
            title="Dragonrider Bow",
            description="Longbow dos Dragonriders, que serviram ao Velho Rei da Car??ncia. Os Dragonriders eram a guarda real do Velho Rei, e grande for??a era exigida deles. Simplesmente puxar este arco requer for??a desumana. Os poucos dignos que podem dominar este arco, entretanto, usam-no para um efeito devastador.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Pun????o de habilidade: Puxe a flecha ainda mais para tr??s para um tiro mais poderoso, que tamb??m pode perfurar escudos.", value="Encontrado no Castelo De Lothric.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:dragonrider-bow/Dragonrider-Bow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_FB")
      async def A_FB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927386699498135632/unknown.png"
      

            embed = discord.Embed(
            title="Flynn's Bows",
            description="Shortbow pertenceu a Flynn, o ladr??o elogiado. A sorte ajusta o poder deste arco. Flynn era conhecido por sua sorte inexplic??vel, e seu arco n??o era exce????o a esse tra??o.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Rapid Fire: Rapidamente posiciona as flechas com sutileza ap??s puxar o arco, permitindo tiros consecutivos.", value="Transposi????o do Thieves' Pact em troca de 10 Lost Trinket e 24.000 almas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:flynn-s-bow/Flynn-s-Bow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_LB")
      async def A_LB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927388132431786034/unknown.png"
      

            embed = discord.Embed(
            title="Longbow",
            description="Arco longo comumente usado por ca??adores. As flechas devem ser equipadas para usar arcos. At?? dois tipos de flechas podem ser equipados ao mesmo tempo e podem ser trocados conforme necess??rio.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Puncture: Puxe a flecha ainda mais para tr??s para um tiro mais poderoso, que tamb??m pode perfurar escudos.", value="Vendido pelo ferreiro Andre por 3.500 almas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:longbow/Longbow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_SHB")
      async def A_SHB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927392619292655726/unknown.png"
      

            embed = discord.Embed(
            title="Scholar's Bow",
            description="Arco curto composto impregnado de magia de cristal. Seu tamanho permite fotos r??pidas. A intelig??ncia ajusta a pot??ncia deste arco. Efeito: aumenta o FP m??ximo em 5%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Rapid Fire: Rapidamente posiciona as flechas com sutileza ap??s puxar o arco, permitindo tiros consecutivos.", value="Firelink - Transposto da Alma de um S??bio de Cristal.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:scholar-s-bow/scholar-s-bow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_SB")
      async def A_SB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927394638682267648/unknown.png"
      

            embed = discord.Embed(
            title="Short Bow",
            description="Arco pequeno padr??o. Seu tamanho permite fotos r??pidas. As flechas devem ser equipadas para usar arcos. At?? dois tipos de flechas podem ser equipados ao mesmo tempo e podem ser alternados conforme necess??rio.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Rapid Fire: Rapidamente posiciona as flechas com sutileza ap??s puxar o arco, permitindo tiros consecutivos.", value="Vendido pelo ferreiro Andre por 1.000 almas. Vendido por Greirat do Undead Settlement por 1,000 Souls depois de derrotar Curse-rotted Greatwood. Equipamento inicial da classe Assassin.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:short-bow/Short-Bow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_WBB")
      async def A_WBB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/927679114096312330/unknown.png"
      

            embed = discord.Embed(
            title="White Birch Bow",
            description="Um arco curto feito com b??tula branca. Dotado de magia de manipula????o de luz. O arco ?? uma rel??quia de uma antiga terra de feiti??arias que foi engolida pelo Abismo, mais conhecida por seu conto popular do her??ico Abysswalker.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Wrathful Arrow: Flechas disparadas por grandes pux??es do arco s??o encantadas com um feiti??o col??rico que as torna quase invis??veis e, com o impacto, cria uma poderosa onda de choque.", value="Firelink Shrine - Transposto com a alma de Halflight")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:white-birch-bow/white_birch_bow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_G_BC")
      async def G_BC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/930113129705259008/unknown.png"
      

            embed = discord.Embed(
            title="Beast Claw",
            description="Arma bestial empunhada pelos irreverentes. Criado por esculpindo os ossos longos de uma besta morta-viva e prendendo-os ?? arma. Os ossos ainda est??o vivos e, quando liberados, concedem ao seu portador um jorro de poder bestial. Efeito: cada acerto aumenta o dano da arma em 1%, com dura????o de 60 segundos. Pilhas. Tamb??m substitui esquiva por Beast Lunge se ativado em Benjin. Desativado se a carga atual do equipamento estiver acima de 70% do m??x.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Bestial Pounce: Ataque os inimigos com ferocidade bestial, causando dano pesado e derrubando-os.", value="Equipamento inicial da classe Madman. Encontrado em Farron Keep.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:beast-claw/beast-claw.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_G_C")
      async def G_C(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/930131944816124004/unknown.png"
      

            embed = discord.Embed(
            title="Claw",
            description="Arma preferida por intelig??ncias de uma terra oriental. As lacera????es que inflige n??o se curam facilmente. Quando com as duas m??os, as garras s??o equipadas em cada m??o.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Stance: Enquanto na postura, use o ataque normal para atacar rapidamente os inimigos com grande ferocidade e ataque forte para deslizar para cima e rasgar a carne do osso.", value="Vendido pelo ferreiro Andre por 1.000 almas. equipamento da classe Brawler.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:claw/Claw.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_G_CC")
      async def G_CC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/930133586961645608/unknown.png"
      

            embed = discord.Embed(
            title="Crab Claw",
            description="Um par de garras de caranguejo feitas de os restos de um caranguejo gigante. ??speras e texturizadas, essas garras d??o uma boa surra de perto. sA apar??ncia desta arma ?? afetada pela infus??o de Frost.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Crabby: Desencadeie uma enxurrada de golpes, contornando a guarda do inimigo.", value="Equipamento inicial da classe Crab King. Dropado por um Caranguejo Menor na Estrada dos Sacrif??cios.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:crab-claw/crab-claw.pngs")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_G_CT")
      async def G_CT(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/930135317250469908/unknown.png"
      

            embed = discord.Embed(
            title="Crow Talons",
            description="Garras usadas pelos Cavaleiros Corvian. Inflige cinco cortes perpendiculares, causando sangramento intenso. sEm sua paix??o pela irm?? Friede, os Cavaleiros Corvian juraram proteger a pintura do fogo e, para isso, levaram ?? execu????o de seus pr??prios irm??os.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Raptor Flurry: Espalhe as garras direita e esquerda como um amplo conjunto de asas e lance em um tornado de ataques consecutivos.", value="Dropado por um M??mico encontrado no Mundo Pintado de Ariandel.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:crow-talons/Crow-Talons.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_G_MC")
      async def G_MC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/930616760716124160/unknown.png"
      

            embed = discord.Embed(
            title="Manikin Claws",
            description="Arma dos Pale Shades, assassinos da Igreja de Londor. As garras curvas causam sangramento intenso. Quando com as duas m??os, as garras s??o equipadas em cada m??o.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Leaping Slash: Execute um golpe de salto para a frente na cabe??a do oponente. Quando bem sucedido, funciona como um tiro na cabe??a, causando grandes danos.", value="Vendido por Marvelous Chester por 6.000 almas. Largada de Londor Pale Shade, que invade Farron Keep e Irithyll do Vale Boreal.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:manikin-claws/Manikin-Claws.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_CB_AB")
      async def CB_AB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931013526976344104/unknown.png"
      

            embed = discord.Embed(
            title="Arbalest",
            description="A maior besta e adequadamente poderosa para seu tamanho. A corda do arco ?? feita de metal, exigindo grande for??a para disparar.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Tackle: Estocada em um tackle de ombro, empurrando os inimigos para tr??s para criar dist??ncia.", value="Encontrado na Catedral das Profundezas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:arbalest/Arbalest.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_CB_AV")
      async def CB_AV(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931015313527562240/unknown.png"
      

            embed = discord.Embed(
            title="Avelyn",
            description="Uma besta de tiro r??pido extremamente rara. Dispara tr??s raios sucessivos por meio de um mecanismo elaborado. Cause dano pesado fazendo valer os tr??s tiros. Apesar de seu uso como arma, esta besta tamb??m ?? uma obra de arte inestim??vel, e tem semelhan??a com um instrumento musical.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Tackle: Estocada em um tackle de ombro, empurrando os inimigos para tr??s para criar dist??ncia.", value="Dropado por um M??mico encontrado na Muralha Alta de Lothric.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:avelyn/Avelyn.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_CB_BC")
      async def CB_BC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931162683464622080/unknown.png"
      

            embed = discord.Embed(
            title="Birch Crossbow",
            description="Besta padr??o empunhada por soldados comuns. Deve ser preparado antes do disparo. Os Dardos devem ser equipados para usar bestas. At?? dois tipos de parafusos podem ser equipados de cada vez, e estes podem ser alternados conforme necess??rio.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Tackle: Estocada em um tackle de ombro, empurrando os inimigos para tr??s para criar dist??ncia.", value="Vendido pelo ferreiro Andre por 1.000 almas. Vendido por Greirat do assentamento de mortos-vivos por 1.000 almas. equipamento da classe Soldado.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:birch-crossbow/birch-crossbow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_CB_KC")
      async def CB_KC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931166330168680499/unknown.png"
      

            embed = discord.Embed(
            title="Knight's Crossbow",
            description="Besta usada pelos orgulhosos cavaleiros de Lothric. Ele tem um elaborado design de ouro. A besta foi aben??oada com o poder do rel??mpago, em antecipa????o ao uso de Lightning Bolts.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Tackle: Estocada em um tackle de ombro, empurrando os inimigos para tr??s para criar dist??ncia.", value="Vendido por Greirat do Undead Settlement por 3.000 almas depois de derrotar o Pont??fice Sulyvahn. Encontrado na Muralha Alta de Lothric.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:knight-s-crossbow/Knight-s-Crossbow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_CB_OC")
      async def CB_OC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931269615953260624/unknown.png"
      

            embed = discord.Embed(
            title="Oak Crossbow",
            description="Uma besta grande e poderosa. Deve ser preparado antes do disparo. Os Dardos devem ser equipados para usar bestas. At?? dois tipos de parafusos podem ser equipados de cada vez, e estes podem ser trocados conforme necess??rio.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Tackle: Estocada em um tackle de ombro, empurrando os inimigos para tr??s para criar dist??ncia.", value="Vendido pelo ferreiro Andre por 3.000 almas. equipamento inicial da classe do ca??ador. Dropado por um Cavaleiro da Catedral encontrado na Catedral das Profundezas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:oak-crossbow/oak-crossbow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_CB_RC")
      async def CB_RC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931326710186639420/unknown.png"
      

            embed = discord.Embed(
            title="Repeating Crossbow",
            description="Esta besta, personalizada para disparos repetidos para enfrentar mobs sozinho, foi empunhada pelo Slave Knight Gael. Usada nas batalhas de uma jornada sem fim, esta besta ?? coberta de tor????es e arranh??es, enferrujada com sangue e extremamente quebradi??a pelo uso excessivo.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Repetir Fogo: Assuma a postura para ativar o mecanismo de disparo repetido e repita o disparo com ataques normais e fortes.", value="Firelink Shrine - Transposto da Soul of Slave Knight Gael")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:repeating-crossbow/repeating_crossbow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_CB_SC")
      async def CB_SC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931327692815601754/unknown.png"
      

            embed = discord.Embed(
            title="Sniper Crossbow",
            description="Besta pesada de longo alcance usada pelos franco-atiradores Carim. Sua base longa dificulta a mira, e o uso preciso requer uma m??o treinada e h??bil.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Tackle: Estocada em um tackle de ombro, empurrando os inimigos para tr??s para criar dist??ncia.", value="Vendido pelo Ferreiro Andre por 6.000 Almas depois de derrotar os Vigilantes do Abismo. Encontrado no Castelo Lothric.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:sniper-crossbow/Sniper-Crossbow.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_BS")
      async def EC_BS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931603169925034054/unknown.png"
      

            embed = discord.Embed(
            title="Beasthunter Saif",
            description="Uma l??mina de ferro grossa usada para cortar a carne de animais. Usado pelos trabalhadores do Undead Settlement para afastar as feras. Efeito: substitui a esquiva por Hunter Dash se ativado em Benjin. Desativado se a carga atual do equipamento estiver acima de 70% do m??x.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Hunter's Fury: Salte para tr??s com um ataque para ganhar dist??ncia e, em seguida, corra de volta com um ataque leve para um golpe r??pido ou um ataque pesado para um golpe esmagador.", value="Vendido pelo Mestre Benjin por 20.000 almas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:beasthunter-saif/beasthunter-saif.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_B")
      async def EC_B(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931603272186355782/unknown.png"
      

            embed = discord.Embed(
            title="Blind",
            description="Uma espada curva com uma l??mina clara. Amplamente conhecido junto com a coragem do cavaleiro de ouro fosco, ?? considerado um dos tesouros de Vinland. A l??mina ?? ilus??ria e leve como uma pena, permitindo que ela passe pelas defesas de qualquer escudo. Efeito: reduz o equil??brio em 50% por 15 segundos ao acertar. Pilhas.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Dropado por um M??mico encontrado no Castelo Lothric.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:blind/blind.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_BB")
      async def EC_BB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931603432735932426/unknown.png"
      

            embed = discord.Embed(
            title="Burial Blade",
            description="Uma arma magistral, usada por um ca??ador decr??pito para lutar contra um pesadelo angustiante. Efeito: substitui a esquiva por Hunter Dash se ativado em Benjin. Desativado se a carga atual do equipamento estiver acima de 70% do m??x.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade F??ria do Redemoinho: Um ataque em cadeia que se encaixa abaixo dos inimigos e balan??a para cima, quebrando a guarda deles. Siga com um ataque forte para cortar o inimigo em um padr??o de corte cruzado.", value="Vendido pelo Mestre Benjin por 32.000 almas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:burial-blade/burial-blade.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_CCS")
      async def EC_CCS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931603591637139476/unknown.png"
      

            embed = discord.Embed(
            title="Carthus Curved Sword",
            description="Espada curva dos espadachins de Carthus. A l??mina grossa e pesada desta arma ?? trabalhada para causar sangramento e requer ampla for??a e destreza para empunhar efetivamente, sugerindo que os espadachins de Carthus estavam entre os mais poderosos.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Vendido pelo Ferreiro Andre por 4.000 Almas depois de derrotar o Lord Wolnir. equipamento da classe Carthus Warrior. Dropado por um Espadachim de Carthus encontrado nas Catacumbas de Carthus.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:carthus-curved-sword/Carthus-Curved-Sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_CS")
      async def EC_CS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931603830662103101/unknown.png"
      

            embed = discord.Embed(
            title="Carthus Shotel",
            description="Espada estranhamente curva criada para causar sangramento, empunhada por espadachins de Carthus. Moldada para se esgueirar pelas defesas dos escudos, esta espada requer ampla destreza para empunhar com efic??cia.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Carthus Cunning: Salte no ar e jogue quatro facas dilacerantes nos inimigos, causando 15 de sangramento para cada faca, pode ser seguido por um ataque leve para liberar mais duas facas, ou um ataque pesado para atacar os inimigos e perfurar as defesas. Aos olhos dos guerreiros de Carthus, nenhum caminho para a vit??ria era desonroso.", value="Vendido pelo Ferreiro Andre por 5.000 Almas depois de derrotar o Gr??o-Senhor Wolnir. Equipamento da classe Carthus Warrior. Dropado por um Grave Warden Skeleton encontrado nas Catacumbas de Carthus.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:carthus-shotel/Carthus-Shotel.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_CMS")
      async def EC_CMS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931603953257427015/unknown.png"
      

            embed = discord.Embed(
            title="Crescent Moon Sword",
            description="A arma de escolha de Ringfinger Leonhard, um tipo de shotel imbu??do do poder da lua. Leonhard partiu em uma jornada de renascimento, mas decidiu servir a deusa como cavaleiro e herdou essa arma.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade L??mina Crescente: Assuma uma postura ampla e dispare as l??minas da lua crescente.", value="Vendido pelo Ferreiro Andre por 30.000 Almas depois de derrotar Aldrich, Devorador de Deuses. Dropado por Ringfinger Leonhard em Anor Londo quando morto ap??s usar o Black Eye Orb. Requer progress??o atrav??s de sua linha de miss??es.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:crescent-moon-sword/Crescent-Moon-Sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_F")
      async def EC_F(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931604083184382002/unknown.png"
      

            embed = discord.Embed(
            title="Falchion",
            description="Espada curva padr??o e arma de corte amplamente utilizada. Os ataques cortantes do falchion s??o bastante comprometidos contra armaduras e peles duras cobertas de escamas.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Vendido pelo Ferreiro Andre por 3.000 Almas")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:falchion/Falchion.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_FS")
      async def EC_FS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/931604217813168129/unknown.png"
      

            embed = discord.Embed(
            title="Follower Sabre",
            description="Grande espada curva empunhada por Farron Followers. Seu grande peso permite ataques em cadeia com m??o pesada.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Skill Prying Wedge: Um ataque em cadeia que se encaixa abaixo dos inimigos e balan??a para cima, quebrando a guarda deles. Um ataque forte pode ser usado para acompanhar o ataque com um golpe fatal.", value="Vendido pelo Ferreiro Andre por 6.000 Almas depois de derrotar a Irm?? Friede. Dropado por um Seguidor de Farron encontrado no Mundo Pintado de Ariandel.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:follower-sabre/Follower-Sabre.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_M")
      async def EC_M(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/932328584100577310/unknown.png"
      

            embed = discord.Embed(
            title="Machete",
            description="Este fac??o tem um ataque de corte e ?? uma ferramenta de trabalho no Undead Settlement. Esta ferramenta de desmontagem n??o foi originalmente projetada para uso em batalha.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Afiar: A l??mina aumenta o HP restaurado a cada acerto bem-sucedido.", value="Vendido pelo Ferreiro Andre por 6.000 Almas depois de derrotar a Irm?? Friede. Dropado por um Seguidor de Farron encontrado no Mundo Pintado de Ariandel.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:machete/Machete.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_PGC")
      async def EC_PGC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/932367531744854128/unknown.png"
      

            embed = discord.Embed(
            title="Painting Guardian's Curved Sword",
            description="Uma arma descrita em lendas transmitidas entre hereges, empunhada pelos Guardi??es da Pintura. Uma arma de formato ??nico com uma ponta plana.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidades Chained Dance: Execute ataques consecutivos implac??veis ??????enquanto tra??a um c??rculo em uma dan??a ??nica de gra??a mortal.", value="Dropado por um M??mico encontrado em Irithyll do Vale Boreal.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:painting-guardian-s-curved-sword/Painting-Guardian-s-Curved-Sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_PKCS")
      async def EC_PKCS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/932375058100396042/unknown.png"
      

            embed = discord.Embed(
            title="Pontiff Knight Curved Sword",
            description="Espada curva empunhada pelos cavaleiros do pont??fice, esp??ritos fr??gidos que permanecem em Irithyll. A grande l??mina parece ser comida por insetos, tornando-a leve, mas tamb??m quebradi??a.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade L??mina de Gelo: Execute um grande movimento girat??rio para imbuir a l??mina com gelo e continue com um ataque forte que corta com uma l??mina gigante feita de gelo.", value="Vendido por Greirat do Undead Settlement por 6.000 Souls depois de derrotar a Cursed-rotted Greatwood. Deixado por um Pont??fice Cavaleiro encontrado em Irithyll do Vale Boreal.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:pontiff-knight-curved-sword/Pontiff-Knight-Curved-Sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_QFS")
      async def EC_QFS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/933494842598785064/unknown.png"
      

            embed = discord.Embed(
            title="Quelaag's Fury Sword",
            description="Uma espada curva nascida da alma de Quelaag, filha da Bruxa de Izalith, que foi transformado em um dem??nio do caos. Como o corpo de Quelaag, a espada apresenta conchas, espinhos e uma camada de fogo do caos.Efeito: Reduz a absor????o de fogo em 1% por 5 segundos. Stacka.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Quelaag's Fury: Enfie a espada na terra, liberando o caos indom??vel. Uma vez que aterrissou, o fogo do caos permanece.", value="Encontrado no Lago Fumegante, requer recarregar a ??rea depois de matar o Velho Rei Dem??nio.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:quelaag-s-fury-sword/quelaag-s-fury-sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_RGCS")
      async def EC_RGCS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/933894089894678529/unknown.png"
      

            embed = discord.Embed(
            title="Rotten Ghru Curved Sword",
            description="Uma espada curvada e meio podre. Arma preferida dos Ghrus de chifres rombudos, descendentes dos ac??litos da Fortaleza Farron. A l??mina ran??osa est?? encharcada de res??duos podres, tornando-a extremamente venenosa.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Vendido pelo Ferreiro Andre por 6.000 Almas depois de derrotar os Vigilantes do Abismo. Dropado por um Ghru encontrado em Farron Keep.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:rotten-ghru-curved-sword/Rotten-Ghru-Curved-Sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_S")
      async def EC_S(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/933894762707185764/unknown.png"
      

            embed = discord.Embed(
            title="Scimitar",
            description="Pequena espada curva que se destaca em movimentos r??pidos e ataques consecutivos. Os ataques cortantes da cimitarra s??o bastante comprometidos contra armaduras e peles duras cobertas de escamas.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Vendido pelo Ferreiro Andre por 600 Almas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:scimitar/Scimitar.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_SH")
      async def EC_SH(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/934080998596034561/unknown.png"
      

            embed = discord.Embed(
            title="Shotel",
            description="Espada amplamente curvada conhecida como a arma favorita do tr??gico Cavaleiro Abra??ado. Moldada para se esgueirar pelas defesas dos escudos, esta espada requer ampla destreza para empunhar com efic??cia.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Vendido pelo Ferreiro Andre por 4.000 Almas. Vendido por Unbreakable Patches por 4.000 almas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:shotel/Shotel.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_SCS")
      async def EC_SCS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/934081960232501288/unknown.png"
      

            embed = discord.Embed(
            title="Smouldering Curved Sword",
            description="Uma espada curvada em chamas empunhada por os ghru que habitam as catacumbas abaixo do lago fumegante. Enlouquecidos pelo calor, esses ghru tornaram-se malformados abomina????es de seus primos no p??ntano de Farron. Efeito: aumenta a absor????o de fogo em 5%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Dropado por um Ghru Fumegante encontrado no Lago Fumegante.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:smouldering-curved-sword/smouldering-curved-sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_SCC")
      async def EC_SCC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/934085589781864498/unknown.png"
      

            embed = discord.Embed(
            title="Storm Curved Sword",
            description="Espada curvada imbu??da da for??a do Stormdrake. O Nameless King, aliado dos drag??es antigos, lutou ao lado do Stormdrake em in??meras batalhas. Quando a grande besta caiu, o rei reivindicou sua alma, como era costume na era dos deuses.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Tornado: Imbui a l??mina com a ira da tempestade em um movimento girat??rio e segue com um forte ataque para suportar essa ira sobre os inimigos.", value="Firelink Shrine - Transposto pela alma do Nameless King.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:storm-curved-sword/Storm-Curved-Sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_EC_WM")
      async def EC_WM(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/934087964101845032/unknown.png"
      

            embed = discord.Embed(
            title="Worker Machete",
            description="Este fac??o tem a forma de uma l??mina e ?? uma ferramenta de trabalho no assentamento de mortos-vivos. N??o originalmente destinado ?? batalha, mas serve como uma arma mortal devido ?? sua ponta afiada.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Encontrado em Undead Settlement.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:worker-machete/worker-machete.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_ECG_CCG")
      async def ECG_CCG(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/934486108258074717/unknown.png"
      

            embed = discord.Embed(
            title="Carthus Curved Greatsword",
            description="Grande espada curva empunhada por espadachins de Carthus. A mais leve das espadas curvas. Feito para causar sangramento.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Vendido pelo Ferreiro Andre por 8.000 Almas depois de derrotar o Gr??o-Senhor Wolnir. Dropado por um Espadachim de Carthus encontrado nas Catacumbas de Carthus.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:carthus-curved-greatsword/Carthus-Curved-Greatsword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_ECG_EG")
      async def ECG_EG(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/934583842956783616/unknown.png"
      

            embed = discord.Embed(
            title="Exile Greatsword",
            description="Espada larga manchada de sangue empunhada por um dos C??es de Guarda de Farron, que preside o sono dos guerreiros ca??dos. A l??mina ?? um lembrete dos crimes passados ??????do exilado. For??a desumana ?? necess??ria para empunhar esta espada grande curvada mais pesada.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Dropado pelo Unkindled Watchdog empunhando-o em Road of Sacrifices. A fogueira mais pr??xima ?? a Halfway Fortress/Farron Keep.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:exile-greatsword/Exile-Greatsword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_ECG_GS")
      async def ECG_GS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/934967169484193842/unknown.png"
      

            embed = discord.Embed(
            title="Gravelord Sword",
            description="Espada empunhada apenas por servos de Gravelord Nito, o primeiro dos mortos. Criado a partir dos ossos dos ca??dos. O miasma da morte exala da espada, uma verdadeira toxina para qualquer ser vivo.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Encontrado nas Catacumbas de Carthus")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:gravelord-sword/gravelord-sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_ECG_HCG")
      async def ECG_HCG(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935246558461583410/unknown.png"
      

            embed = discord.Embed(
            title="Harald Curved Greatsword",
            description="Espada curva gigante decorada com ouro empunhada por guerreiros da Legi??o Harald, que buscavam oalma escura. As espadas afundaram no escuro com a legi??o, onde suas l??minas foram severamente corro??das.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Sever: Segure a l??mina gigante com as duas m??os e corte repetidamente aos p??s do inimigo.", value="Dropado por um Harald Knight encontrado em The Dreg Heap.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:harald-curved-greatsword/harald_curved_greatsword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_ECG_M")
      async def ECG_M(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935251500366725150/unknown.png"
      

            embed = discord.Embed(
            title="Murakumo",
            description="A grande espada curva de Alva, Buscadora dos Rejeitados, especialmente forjada em uma terra oriental. Afiada, mas pesada, esta espada requer extrema for??a e destreza para empunhar. A busca pelos rejeitados n??o tinha fim, e assim o cavaleiro viajante se aqueceu com uma arma mais deformada.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Vendido pelo Ferreiro Andre por 15.000 Almas depois de derrotar Yhorm, o Gigante. Equipamento da classe Wayfarer. Dropado por Dark Spirit Alva, Seeker of the Spurned em Irithyll Dungeon.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:murakumo/Murakumo.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_ECG_OWCS")
      async def ECG_OWCS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935255171062190181/unknown.png"
      

            embed = discord.Embed(
            title="Old Wolf Curved Sword",
            description="Espada curvada com a alma do velho lobo que fica com os c??es de guarda de Farron. Efeito: Aumenta o dano contra inimigos abissais em 20%. Recupera HP com ataques sucessivos, restaurando 2% + 75 HP por ataque uma vez acionado.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Salto do Lobo: Fatie os inimigos com um grande movimento girat??rio, depois salte para fora do caminho do perigo e siga com um ataque forte", value="Watchdogs of Farron transposi????o em troca de 15 Wolf's Blood Swordgrass e 16.000 Souls.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:old-wolf-curved-sword/Old-Wolf-Curved-Sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_ECG_PKG")
      async def ECG_PKG(self, ctx):
            url_image="https://media.discordapp.net/attachments/925612211479642212/935256725957800026/unknown.png"
      

            embed = discord.Embed(
            title="Pontiff Knight Greatsword",
            description="Espada grande curva empunhada pelos cavaleiros do pont??fice, esp??ritos fr??gidos que permanecem em Irithyll. A grande l??mina parece ser comida por insetos, tornando-a leve, mas tamb??m quebradi??a.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade L??mina de Gelo: Execute um grande movimento girat??rio para imbuir a l??mina com gelo e continue com um ataque forte que corta com uma l??mina gigante feita de gelo.", value="Encontrada em Irithyll of the Boreal Valley.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:pontiff-knight-greatsword/Pontiff-Knight-Greatsword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_ECG_S")
      async def ECG_S(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935262302276579388/unknown.png"
      

            embed = discord.Embed(
            title="Server",
            description="Uma espada grande curva usada em um misterioso rito antigo. Imbu??do de uma energia her??tica assustadora esta espada absorve HP ap??s a morte de um inimigo. Efeito: absorve 1,5% de HP ao acertar.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Spin Slash: Corte os inimigos com um grande movimento girat??rio e siga com um ataque forte para um corte vertical girat??rio.", value="Encontrada em Undead Settlement.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:server/server.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_AD")
      async def A_AD(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935278645528903800/unknown.png"
      

            embed = discord.Embed(
            title="Aquamarine Dagger",
            description="Uma adaga equipada com cristal de ??gua-marinha. Gravado com uma ora????o na l??ngua antiga para evitar incidentes. Talvez fosse um presente de despedida dado a algu??m enviado em grandes viagens.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade L??mina de CristaL: Libere a magia dos cristais de ??gua-marinha, criando uma l??mina de cristal azul fugaz, longa o suficiente para balan??ar como uma espada reta.", value="Encontrada em The Dreg Heap.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:aquamarine-dagger/aquamarine_dagger.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_BK")
      async def A_BK(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935311168208269432/unknown.png"
      

            embed = discord.Embed(
            title="Bandit's Knife",
            description="Uma espada curta de um ??nico gume. Principalmente uma arma de corte, mas sua l??mina ?? criado para causar sangramento, tornando-o um favorito de ladr??es e bandidos humildes",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Passo R??pido: Instantaneamente passo atr??s ou ao redor do lado dos inimigos. Especialmente eficaz quando travado no alvo.", value="Vendido pelo ferreiro Andre por 1.500 almas. Vendido por Greirat do assentamento de mortos-vivos por 1.500 almas.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:bandit-s-knife/Bandit-s-Knife.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_CG")
      async def A_CG(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935330609742643230/unknown.png"
      

            embed = discord.Embed(
            title="Corvian Greatknife",
            description="Adaga dos indesejados, daqueles guiados por contadores de hist??rias her??ticos. Manchado pelo lodo nocivo encontrado em Farron Keep. Uma adaga bastante grande com um ataque poderoso, mas essa tentativa transparente de intimidar os inimigos revela muito sobre os medos de seu dono.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Ponto Cego: Use contra inimigos protegidos para romper sua guarda atacando de lado.", value="Vendido por Blacksmith Andre por 3.000 Souls depois de derrotar os Abyss Watchers. Dropado por um Corvian na Estrada dos Sacrif??cios.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:corvian-greatknife/Corvian-Greatknife.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_D")
      async def A_D(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935333204594921492/unknown.png"
      

            embed = discord.Embed(
            title="Dagger",
            description="Adaga pequena padr??o. Adagas pequenas n??o t??m poder ou alcance, mas podem causar acertos consecutivos r??pidos devido ao seu peso leve. Altamente eficaz quando usado para acertos cr??ticos, como ap??s aparar ou atacar por tr??s.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Passo R??pido: Instantaneamente passo atr??s ou ao redor do lado dos inimigos. Especialmente eficaz quando travado no alvo.", value="Vendido pelo ferreiro Andr?? por 300 almas. Equipamento inicial da classe Huntsman. Equipamento inicial da classe Sorcerer.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:dagger/Dagger.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_ED")
      async def A_ED(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935342248009297920/unknown.png"
      

            embed = discord.Embed(
            title="Engraved Dagger",
            description="Uma adaga gravada com um desenho ornamentado. Diz-se ser a heran??a da realeza, est?? imbu??da de poder sagrado. Efeito: aumenta a F?? em 5. Aumenta o dano contra inimigos mortos-vivos em 5% e evita a remontagem do esqueleto.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Ira Sagrada: Assuma a postura para imbuir a arma com luz sagrada e use um ataque forte para liberar a luz junto com um grande impulso da arma.", value="Encontrado em Lothric Castle.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:engraved-dagger/engraved-dagger.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_FD")
      async def A_FD(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935554617947865148/unknown.png"
      

            embed = discord.Embed(
            title="Firelink Dagger",
            description="Os Lords of Cinder ligaram a Primeira Chama, e esta Adaga foi empunhada por sua manifesta????o divina. Efeito: aumenta o HP m??ximo, FP e Stamina em 5%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Parry: Desvie facilmente de um ataque e siga com um acerto cr??tico. Funciona enquanto equipado em ambas as m??os.", value="Firelink Shrine - Transposto da Soul of the Lords.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:firelink-dagger/Firelink-Dagger.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_F")
      async def A_F(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935581139287035904/unknown.png"
      

            embed = discord.Embed(
            title="Frostfall",
            description="Adaga tecida por feiti??os da lend??ria Odessa do norte de Forossan. Depois que Forossa desmoronou, Odessa seguiu o Rei do Marfim at?? Eleum Loyce tornando-se seu s??bio mais confi??vel. Quando o reino caiu em ru??nas, ela manteve seu rei at?? o fim, finalmente pulando ao lado dele nas profundezas do antigo caos. A l??mina agora zumbe com gelo e fogo. Efeito: A queda de gelo combina com os golpes do portador. Tamb??m substitui a esquiva por Hunter Dash se habilitada em Benjin. Desativado se a carga atual do equipamento estiver acima de 70% do m??x.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Inverno sem fim: Assuma a postura dos nortenhos. Use o ataque normal para invocar os ventos penetrantes de Eleum Loyce, ataque forte para invocar a l??mina do Rei do Marfim pervertida pelo fogo gelado, ou ataque esquerdo para desencadear um ataque de lan??as da alma.", value="Firelink Shrine - Transposto da Soul of Princess Yngvil.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:frostfall/Frostfall.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_HD")
      async def A_HD(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935587571885572116/unknown.png"
      

            embed = discord.Embed(
            title="Handmaid's Dagger",
            description="Adaga usada pelas servas da Capital Profanada. Diz-se que essas mulheres tinham prazer em ferir os outros. Efeito: reduz todo o custo de FP de feiti??os em 10%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Ponto Cego: Use contra inimigos protegidos para romper sua guarda atacando de lado.", value="Dropado por uma Serva Carcereira encontrada na Capital Profanada.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:handmaid-s-dagger/Handmaid-s-Dagger.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_H")
      async def A_H(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935590898723618876/unknown.png"
      

            embed = discord.Embed(
            title="Harpe",
            description="O grande corpo em forma de foice, usado para cortar cad??veres, ?? uma ferramenta de trabalho no assentamento de mortos-vivos. A ponta afiada est?? na parte interna da arma, projetada para cortar e puxar, permitindo assim um bom dano contra inimigos protegidos.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Passo R??pido: Instantaneamente passo atr??s ou ao redor do lado dos inimigos. Especialmente eficaz quando travado no alvo.", value="Vendido pelo Ferreiro Andre por 1.400 almas depois de derrotar o Greatwood apodrecido por maldi????o. Equipamento da classe Herege. Encontrado no assentamento de mortos-vivos.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:harpe/Harpe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_KB")
      async def A_KB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935592001661964288/unknown.png"
      

            embed = discord.Embed(
            title="Kris Blade",
            description="Uma pequena espada cerimonial. Runas antigas s??o habilmente esculpidas na l??mina. Usado como uma ajuda para encantamentos. Efeito: aumenta o dano m??gico em 5%, mas reduz a absor????o de Magia, Fogo, Raio e Escurid??o em 20%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Ponto Cego: Use contra inimigos protegidos para romper sua guarda atacando de lado.", value="Dropado por um M??mico encontrado em Irithyll do Vale Boreal.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:kris-blade/kris-blade.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_MB")
      async def A_MB(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935593078054584330/unknown.png"
      

            embed = discord.Embed(
            title="Mail Breaker",
            description="Uma pequena espada feita para ataques de empurr??o. Esta espada dura e sem fio pode perfurar armaduras resistentes e possui um ataque cr??tico mortal.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Divisor de Escudo: Mire com cuidado e ataque em uma grande estocada para a frente para perfurar os escudos inimigos e infligir dano diretamente.", value="Vendido pelo ferreiro Andre por 4.000 almas. Sirris of the Sunless Realms oferece um Holy Mail Breaker ao convocar o jogador para seu reino para derrotar Creighton the Wanderer em Irithyll of the Boreal Valley.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:mail-breaker/Mail-Breaker.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_MHS")
      async def A_MHS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935594288040017960/unknown.png"
      

            embed = discord.Embed(
            title="Murky Hand Scythe",
            description="Uma foice de m??o curta empunhada pelos homens das trevas que se erguem das profundezas. Envolto por uma umidade negra e imbu??do da for??a do escuro.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Passo R??pido: Instantaneamente passo atr??s ou ao redor do lado dos inimigos. Especialmente eficaz quando travado no alvo.", value="Dropado cair por um Murkman encontrado em The Dreg Heap.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:murky-hand-scythe/murky_hand_scythe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_NEA")
      async def A_NEA(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935722287443882054/unknown.png"
      

            embed = discord.Embed(
            title="Needle of Eternal Agony",
            description="Uma agulha grande e curva com ferr??es farpados. Esta arma foi forjada a partir dos restos mortais de um maneater. Ele esfaqueia seu alvo, engancha na carne e lentamente tritura sua alma.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Passo R??pido: Instantaneamente passo atr??s ou ao redor do lado dos inimigos. Especialmente eficaz quando travado no alvo.", value="Transposi????o Pilgrims of Dark em troca de 3 Abyssal Fragment e 4.000 Souls. Dropado por um M??mico na Estrada dos Sacrif??cios.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:needle-of-eternal-agony/needle-of-eternal-agony.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_PD")
      async def A_PD(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935725271976394852/unknown.png"
      

            embed = discord.Embed(
            title="Parrying Dagger",
            description="Adaga com uma guarda muito curvada. Uma adaga feita especialmente para aparar que geralmente ?? equipado em um m??o esquerda no lugar de um escudo.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Parry: Desvie facilmente de um ataque e siga com um acerto cr??tico. Funciona enquanto equipado em ambas as m??os.", value="Vendido pelo ferreiro Andre por 2.000 almas. Vendido por Unbreakable Patches por 2.000 almas. Equipamento da classe Royal Swordsman.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:parrying-dagger/Parrying-Dagger.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_RGD")
      async def A_RGD(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/935913153819189258/unknown.png"
      

            embed = discord.Embed(
            title="Rotten Ghru Dagger",
            description="Um punhal bruto e meio podre. Arma preferida dos Ghrus de chifres rombudos, descendentes dos ac??litos da Fortaleza Farron. A l??mina ran??osa est?? encharcada de res??duos podres, tornando-a extremamente venenosa.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Passo R??pido: Instantaneamente passo atr??s ou ao redor do lado dos inimigos. Especialmente eficaz quando travado no alvo.", value="Vendido pelo Ferreiro Andre por 2.000 Almas depois de derrotar os Vigilantes do Abismo. Dropado por um Conjurator Ghru encontrado em Farron Keep.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:rotten-ghru-dagger/Rotten-Ghru-Dagger.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_SS")
      async def A_SS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/936656927201591296/unknown.png"
      

            embed = discord.Embed(
            title="Sage's Stiletto",
            description="Um florete extremamente pequeno. Do tamanho de uma adaga e sem l??mina, est?? imbu??do de magia especial. Usado pelos s??bios enigm??ticos, que s??o conhecidos por seus of??cios m??gicos. Efeito: reduz todo o custo de FP de feiti??os em 10%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Divisor de Escudo: Mire com cuidado e ataque em uma grande estocada para a frente para perfurar os escudos inimigos e infligir dano diretamente.", value="Firelink Shrine - Transposto da Soul of a Crystal Sage.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:sage-s-stiletto/sage-s-stiletto.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_SC")
      async def A_SC(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937065149787963452/unknown.png"
      

            embed = discord.Embed(
            title="Scholar's Candlestick",
            description="Um casti??al coberto de escamas de marfim outrora usado pelos Eruditos dos Grandes Arquivos. Isso serviu como sua luz orientadora, bem como uma ferramenta de autocontrole. Efeito: aumenta o FP m??ximo em 5%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Luz Guia: Uma vela fornece uma fonte tempor??ria de luz, aumentando o dano m??gico em 10% por 30 segundos.", value="Vendido por Greirat do Undead Settlement por 3.500 almas depois de derrotar o Pont??fice Sulyvahn. Dropado pelo iluminado Archive Scholar no Grand Archives em frente ?? primeira po??a de cera.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:scholar-s-candlestick/Scholar-s-Candlestick.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_S")
      async def A_S(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937073326805901313/unknown.png"
      

            embed = discord.Embed(
            title="Shiv",
            description="Uma faca grosseira, empunhada por pobres almas assediadas por est??reis est??pidos. Embora bruta, esta faca ?? f??cil de esconder, permitindo f??cil surpresa ataca antes que um inimigo esteja ciente. Efeito: aumenta a velocidade de movimento em 10%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Ponto Cego: Use contra inimigos protegidos para romper sua guarda atacando de lado.", value="Equipamento inicial da classe Assassin. Encontrado no assentamento de mortos-vivos.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:shiv/shiv.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_SD")
      async def A_SD(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937075331783852132/unknown.png"
      

            embed = discord.Embed(
            title="Smouldering Dagger",
            description="Uma adaga fumegante empunhada por os ghru que habitam as catacumbas abaixo do lago fumegante. Enlouquecidos pelo calor, esses ghru tornaram-se malformados abomina????es de seus primos no p??ntano de Farron. Efeito: aumenta a absor????o de fogo em 5%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Passo R??pido: Instantaneamente passo atr??s ou ao redor do lado dos inimigos. Especialmente eficaz quando travado no alvo.", value="Dropado por um Ghru Conjurador Fumegante encontrado no Lago Fumegante.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:smouldering-dagger/smouldering-dagger.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_TSS")
      async def A_TSS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937736874758398012/unknown.png"
      

            embed = discord.Embed(
            title="Tailbone Short Sword",
            description="Adaga retorcida estimada pelos miser??veis ??????prisioneiros de Irithyll Dungeon. Feito a partir de um c??ccix fr??gil e visto como um sinal dos drag??es. Seus gritos s??o frequentemente ouvidos dentro da masmorra, enquanto eles ingenuamente mutilam sua carne indigna.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Soltar Drag??o: Empurre a adaga para liberar a for??a dos drag??es, semelhante a uma antiga arma de drag??o, apenas com seu poder tragicamente desbotado.", value="Vendido pelo Ferreiro Andre por 5.000 Almas ap??s derrotar Yhorm, o Gigante. Dropado por um Wretch encontrado em Irithyll Dungeon.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:tailbone-short-sword/Tailbone-Short-Sword.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_A_TH")
      async def A_TH(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937739595808927764/unknown.png"
      

            embed = discord.Embed(
            title="Thrall Harpe",
            description="Uma simples harpa empunhada pelos escravos no assentamento de mortos-vivos. Tratados como escravos, os hollows agora conhecidos apenas como Thralls s??o surpreendentemente h??beis em manejar suas ferramentas em combate. Efeito: aumenta a Sorte em 5 e aumenta a dist??ncia do salto em 25%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Passo R??pido: Instantaneamente passo atr??s ou ao redor do lado dos inimigos. Especialmente eficaz quando travado no alvo.", value="Equipamento inicial da classe Atleta. Encontrado no assentamento de mortos-vivos.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:thrall-harpe/thrall-harpe.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_S_C")
      async def S_C(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937743415171502250/unknown.png"
      

            embed = discord.Embed(
            title="Caestus",
            description="A arma de um lutador de punho feito de tiras grossas de couro cravejadas com rebites de ferro. Quando com duas m??os, os caesti s??o equipados em cada m??o.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Postura do Brawler: Enquanto estiver em posi????o, use o ataque normal para deslizar pelo ch??o, desviando dos ataques inimigos e se reposicionando, ou ataque forte para lan??ar um soco carregado devastador. Alcance aumentado quando bloqueado.", value="Vendido pelo ferreiro Andre por 1.000 almas. Equipamento da classe Brawler.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:caestus/Caestus.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_S_DH")
      async def S_DH(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937759905274822676/unknown.png"
      

            embed = discord.Embed(
            title="Dark Hand",
            description="Arma que permite ao seu portador evocar uma arte exclusiva de Londor, a terra do Hollow. Diz-se tamb??m que ?? uma antiga rel??quia de uma Serpente Primordial. A M??o Negra suga impiedosamente a ess??ncia de suas v??timas e tamb??m pode funcionar como um escudo especial. A Absor????o de Guarda desta arma aumenta com a Destreza.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Dreno de Vida: Abrace a v??tima e roube seu HP. S?? pode ser usado contra humanos.", value="Vendido por Yuria de Londor por 12.000 almas. Dropado por um Darkwraith encontrado em Farron Keep.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:dark-hand/Dark-Hand.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_S_DF")
      async def S_DF(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937760512865861672/unknown.png"
      

            embed = discord.Embed(
            title="Demon's Fist",
            description="Um punho demon??aco que queima com ess??ncia de fogo. Seu portador pode liberar este poder atrav??s do uso de sua habilidade. Quando com as duas m??os, os punhos s??o equipados em cada m??o. Emite uma bola de fogo com ataques carregados. Efeito: Reduz a absor????o de fogo em 1% por 5 segundos. Pilhas.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Redemoinho Flamejante: Gire atrav??s de oponentes com abandono, punhos flamejantes estendidos. Usar um ataque forte enquanto gira utiliza seu impulso para bater no ch??o com os dois punhos.", value="Firelink Shrine - Transposto da Alma de um Dem??nio.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:demon-s-fist/Demon-s-Fist.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_S_DBF")
      async def S_DBF(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937852475942260866/unknown.png"
      

            embed = discord.Embed(
            title="Dragon Bone Fist",
            description="Uma arma forjada dos restos do golem de ferro, dito ser o guardi??o da Fortaleza de Sen que repeliu in??meros her??is que buscaram passagem para Anor Londo. Efeito: aumenta a absor????o de fogo em 5%.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Rajada de Punhos: Lance em um tornado de ataques consecutivos.", value="Firelink Shrine - Transposto da Soul of the Ancient Wyvern.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:dragon-bone-fist/dragon-bone-fist.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_S_DRF")
      async def S_DRF(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937890307423481877/unknown.png"
      

            embed = discord.Embed(
            title="Drake Fist",
            description="Um punho retorcido imbu??do do poder remanescente dos dracos, primos distantes dos drag??es. Quando com as duas m??os, os punhos s??o equipados em cada m??o.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Rajada de Punhos: Lance em um tornado de ataques consecutivos.", value="Transposi????o de Dragon Remnants em troca de 10 Dragon Eye e 20.000 Souls. Equipamento inicial da classe Dragon Knight.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:drake-fist/drake-fist.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_S_HG")
      async def S_HG(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937908374648029235/unknown.png"
      

            embed = discord.Embed(
            title="Hands of God",
            description="Uma arma de punho que dizia levar o nome dos deuses. Era uma vez um homem forte que matava drag??es com as pr??prias m??os. Seus punhos divinos lhe renderam quase um status m??tico. Emite uma explos??o de for??a com ataques carregados.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Rajada de Punhos: Lance em um tornado de ataques consecutivos.", value="Equipamento inicial da classe Misantropo. Encontrado no Cemit??rio das Cinzas (requer Point Up).")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:hands-of-god/hands-of-god.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_S_HS")
      async def S_HS(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/937920481082880020/unknown.png"
      

            embed = discord.Embed(
            title="Hands of Sin",
            description="M??os que antes estavam ligadas a uma monstruosidade do pecado. A busca pelo conhecimento ?? repleta de perigos. Para aqueles que se aprofundam demais, espera-se uma transforma????o verdadeiramente horr??vel.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Rajada de Punhos: Lance em um tornado de ataques consecutivos.", value="Encontrado na Capital Profanada.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:hands-of-sin/hands-of-sin.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_MTG_ADH")
      async def MTG_ADH(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/938077649249640448/unknown.png"
      

            embed = discord.Embed(
            title="Ash Demon Hammer",
            description="Um martelo de pedra cinzenta empunhado pelo solit??rio Dem??nio Perdido no topo da ponte em ru??nas encontrada em Farron Keep. O tempo diminuiu a for??a dos dem??nios, mas embora eles mesmos est??o diminuindo, suas armas n??o. Absor????o de Guarda desta arma escala com Destreza e sua Estabilidade com For??a.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Tremor: Forte ataque para levantar a terra, criando uma onda de choque que retumba como um poderoso grito de guerra.", value="Encontrado em Farron Keep.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:ash-demon-hammer/ash-demon-hammer.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_MTG_BL")
      async def MTG_BL(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/938863163200376862/unknown.png"
      

            embed = discord.Embed(
            title="Bloodletter",
            description="A arma demente brandida por Ollis, o infame mercen??rio. Disse para rasgar a carne de suas v??timas, levando a feridas irrevog??veis. Efeito: substitui a esquiva por Hunter Dash se ativado em Benjin. Desativado se a carga atual do equipamento estiver acima de 70% do m??x. A Absor????o de Guarda desta arma escala com Destreza e sua Estabilidade com For??a.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Ira Sangu??nea: Enfie o martelo no ch??o para liberar uma torrente de seu pr??prio sangue que danifica os inimigos pr??ximos e os faz sangrar profusamente, isso tamb??m aumenta o dano em 30% e inflige 20 Sangramento por 60 segundos.", value="Dropado por Ollis, o Impiedoso em Irithyll Dungeon.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:bloodletter/bloodletter.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_MTG_B")
      async def MTG_B(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/938872922259480646/unknown.png"
      

            embed = discord.Embed(
            title="Bramd",
            description="Um martelo de ferro grosseiro terrivelmente enorme, considerado um dos tesouros de Vinland. Sua distor????o ?? a marca de um antigo assassino gigante. Dif??cil de usar mesmo com as duas m??os se o portador tiver for??a humana normal. A Absor????o de Guarda desta arma escala com Destreza e sua Estabilidade com For??a. Efeito: absorve 50 HP ao matar.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Ira Sagrada: Enfie a arma na terra e emita uma poderosa onda de choque.", value="Dropado por um M??mico encontrado na Capital Profanada.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:bramd/bramd.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_MTG_CP")
      async def MTG_CP(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/938942242280865822/unknown.png"
      

            embed = discord.Embed(
            title="Church Pick",
            description="Uma grande picareta de guerra forjada a partir dos contos de antigos ca??adores, que a usavam para ca??ar feras gigantes em nome de sua igreja. Apesar de seu tamanho, ?? uma arma altamente pr??tica. A Absor????o de Guarda desta arma escala com Destreza e sua Estabilidade com For??a. Efeito: substitui a esquiva por Hunter Dash se ativado em Benjin. Desativado se a carga atual do equipamento estiver acima de 70% do m??x.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Corrida Justa: Corra para os inimigos com f??ria justa, depois siga com um ataque normal para quebrar a guarda de um inimigo do fole, ou um ataque forte para derrub??-los no ch??o.", value="Encontrado na Cathedral of the Deep.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:church-pick/church-pick.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      @commands.command(name="arma_MTG_DGH")
      async def MTG_DGH(self, ctx):
            url_image="https://cdn.discordapp.com/attachments/925612211479642212/940296950920659005/unknown.png"
      

            embed = discord.Embed(
            title="Demon's Great Hammer",
            description="Arma demon??aca constru??da a partir das ??rvores de pedra. Usado por dem??nios menores encontrados em um asilo esquecido. Este martelo n??o est?? imbu??do de nenhum poder especial, mas pode alegremente derrotar os inimigos a uma polpa, desde que voc?? tenha a for??a para empunh??-lo. A Absor????o de Guarda desta arma escala com Destreza e sua Estabilidade com For??a.",
            color = 0xFFFFFF  
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
      
            embed.set_footer (text="Creditos por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Habilidade Grito de Guerra :Solte um grito de guerra animado que aumenta temporariamente o ataque em 15% por 20 segundos.", value="Firelink Shrine - Transposto da Alma de um Dem??nio.")
            embed.set_thumbnail (url="http://ds3-cinders.wdfiles.com/local--files/image-set-equipment:demon-s-great-hammer/demon-s-great-hammer.png")
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)
      


def setup(bot):
    bot.add_cog(Armas(bot))        

    print("pronto")