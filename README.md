# ItemStack - 一个物品轮子
> 其实就是仿照bukkit的ItemStack写的

## Something important - 注意事项
请确保你的MCDR支持rtext

## API - 接口
### ItemStack - 物品栈

| 方法 | 作用 | 返回值 |
| ------------ | ------------ | ------------ |
| get_material() | 获得该物品栈的材质 | 类型: str, 该物品栈的材质 |
| set_material(`str`material) | 将该物品栈的材质设置为`material` | 类型: ItemStack, 此ItemStack自身 |
| get_number() | 获取该物品栈的数量 | 类型: int, 该物品栈的数量 |
| set_number(`int`count) | 将该物品栈的数量设置为`count` | 类型: ItemStack, 此ItemStack自身 |
| get_meta() | 获取该物品栈的物品元数据 | 类型: ItemMeta, 该物品堆的物品元数据 |
| set_meta(`str`meta) | 将该物品栈的元数据设置为`meta` | 类型: ItemStack, 此ItemStack自身 |
| give(`server_interface`server, `str`player_name) | 将该物品栈给予`player` | 无 |

### ItemMeta - 物品元数据
懒得写了(不会写)
## Example - 例子
###当玩家进入服务器时给予一根击退棒
```python
from plugins.ItemStack import *
from utils import rtext


def on_player_joined(server, player):
	qwq = ItemStack("minecraft:stick", 1) # 1根木棍(minecraft:stick)
	name = rtext.RTextList(rtext.RText("击", color=rtext.RColor.red, styles=rtext.RStyle.bold),
                           rtext.RText("退", color=rtext.RColor.green, styles=rtext.RStyle.italic),
                           rtext.RText("棒", color=rtext.RColor.blue, styles=rtext.RStyle.bold))
    qwq.get_meta()\
	.set_display_name(name)\ # 设置物品名字
		.add_enchantments(Enchantment.KNOCKBACK, 100)\ # 击退100
		.add_enchantments(Enchantment.SHARPNESS, 50) # 锋利50
	qwq.give(server, player) # 给予玩家
```
长这样
![击退棒](https://github.com/dogdie233/ItemStack/blob/master/%E7%89%A9%E5%93%81%E5%B1%95%E7%A4%BA.png?raw=true "击退棒")

## 更新计划
- 玩家头颅
- 物品属性
- 书
- 工具耐久
- 还有很多

## lazy to update - 自行摸索⑧
### 有bug发issues
