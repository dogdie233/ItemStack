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

# lazy to update - 自行摸索⑧
