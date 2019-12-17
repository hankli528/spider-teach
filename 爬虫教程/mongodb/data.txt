dict_data = {
	"_id":1,
	name:"王五",
	age:55,
	gender:true
}

db.stu.insert(dict_data)

db.stu.insert({_id:1,name:"李四",age:38,gender:true,like:"🐶🐶"})
db.stu.insert({_id:2,name:"张三",age:48,gender:true,like:"🐱🐱"})
db.stu.insert({_id:3,name:"王五",age:58,gender:true,like:"🐔🐔"})
db.stu.insert({_id:4,name:"小红",age:18,gender:false,like:"🐭🐭"})
db.stu.insert({_id:5,name:"小兰",age:28,gender:false,like:"🐶🐶"})
db.stu.insert({_id:6,name:"小明",age:10,gender:true,like:"🐔🐔"})
db.stu.insert({_id:7,name:"小丽",age:30,gender:false,like:"🐔🐔"})

db.stu.insert({_id:8,name:"A",age:30,gender:false,like:"🐔🐔"})

db.stu.insert({_id:9,name:"小明",age:10,gender:true,like:"🐔🐔"})
db.stu.insert({_id:10,name:"小丽",age:30,gender:false,like:"🐔🐔"})




db.stu.find({

	$where:function () {
		return this.age > 20
	}
})

# 聚合查询查询
db.xx.aggregate(
	[
		{管道1},
		{管道2}
	]
)

// $group  分组;  男女分组性别分组
db.stu.aggregate([{$group:{_id:"$gender"}}])

// 表达式 $sum $avg $first $last $max $min $push

// 按照 写别分组 ,求年龄之和
db.stu.aggregate(
	[
		{$group:{_id:"$gender",sumage:{$sum:"$age"}}}
	]
	)
db.stu.aggregate(
	[
		{$group:{_id:"$gender",sumage:{$avg:"$age"}}}
	]
	)

// 按照爱好分组, 求最大值 age
db.stu.aggregate([

	{$group:{_id:"$like",max_age:{$max:"$age"}}}

	])
db.stu.aggregate([

	{$group:{_id:"$like",max_age:{$min:"$age"}}}

	])
db.stu.aggregate([

	{$group:{_id:"$like",max_age:{$first:"$age"}}}

	])
db.stu.aggregate([

	{$group:{_id:"$like",max_age:{$last:"$age"}}}

	])

// 统计 这批人按性别分养的宠物
db.stu.aggregate([
{
	$group:{_id:"$gender",animate:{$push:"$like"}}
}

	])


// $match == find; 区别在于 find 不能使用管道传递

//  宠物是小鸡的 人有哪些?
db.stu.find({like:"🐔🐔"})
db.stu.aggregate([
		{$match:{like:"🐔🐔"}}
	])
// 求 年龄大于20; 男女年龄的平均值
db.stu.aggregate([
	{$match:{age:{$gt:20}}},
	{$group:{_id:"$gender",avgage:{$avg:"$age"}}}

	])


// $project 投影,显示的字段 显示1or true
// 求年龄小于50;求按照爱好分组, 求年龄之和 求年龄平均值,; 只想看之和
db.stu.aggregate([
	{$match:{age:{$lt:50}}},
	{$group:{_id:"$like",sumage:{$sum:"$age"},avgage:{$avg:"$age"}}},
	{$project:{sumage:true}}
	])

// $sort 排序
db.stu.aggregate([
{$sort:{age:-1}}
	])
db.stu.aggregate([
	{$match:{age:{$lt:50}}},
	{$group:{_id:"$like",sumage:{$sum:"$age"},avgage:{$avg:"$age"}}},
	{$project:{sumage:true}},
	{$sort:{sumage:1}}
	])


//  跳过2个 显示5
db.stu.aggregate(
	[
		{$skip:2},
		{$limit:5}

	])

db.stu.aggregate(
	[
		{$limit:5},
		{$skip:2},
	])



// $unwind  拆分列表;  $push
// 男女分组,之后 各自的名字有哪些
db.stu.aggregate([
	{$group:{_id:"$gender",allname:{$push:"$name"}}},
	{$unwind:"$allname"}
	])

// 年龄小于60岁,按照性别分组,取出喜欢的宠物, 拆分文档
db.stu.aggregate(
	[
		{$match:{age:{$lt:60}}},
		{$group:{_id:"$gender",animate:{$push:"$like"}}},
		{$unwind:"$animate"}
	]
	)

// 50W 的数据
for (var i = 0; i <= 500000; i++) {
	
	db.data.insert(
	{
		_id:i,
		user:"user"+i,
		age:i

	})
}

// _id  1毫秒
db.data.find({_id:333333}).explain('executionStats')
// user 222毫秒 -- 1毫秒
db.data.find({user:"user333333"}).explain('executionStats')
// age  227毫秒 --- 0毫秒
db.data.find({age:333333}).explain('executionStats')

// 设置 内容key 为id ;提高查询速度
db.data.ensureIndex({user:1})
db.data.ensureIndex({age:1})

// 查看索引
db.data.getIndexes()

// 删除索引
db.data.dropIndex('key_1')

// 备份数据库
mongodump -h 127.0.0.1:27017 -d five -o /Users/apple/Desktop/beifen 

// 恢复数据库
mongorestore -h 127.0.0.1:27017 -d six --dir /Users/apple/Desktop/beifen/five

// 导出文件
mongoexport -h 127.0.0.1:27017 -d six -c stu -o data.json
mongoexport -h 127.0.0.1:27017 -d six -c stu -o data.csv --type csv -f _id,user,age,like

// 导入文件
mongoimport -h 127.0.0.1:27017  -d seven -c stu --file data.json





