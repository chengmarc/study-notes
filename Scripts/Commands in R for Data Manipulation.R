path_folder = "C:\\Users\\Admin\\Desktop"
file_name = "file_name.csv"

##### Read and Write #####
df = read.csv(paste0(path_folder, file_name))
df = fread(paste0(path_folder, file_name), sep='\t', quote="", fill=TRUE)

write.csv(df, 'Path', row.names=FALSE)
output = list("Tab Name 1"=df1, "Tab Name 2"=df2)
write.xlsx(output, file='Path', row.names=FALSE)

##### Manipulate Data #####
df = df[df$Column_Name == ""] 
df[,'New Column'] = 'value'
df['Date Column'] = as.Date(df['Date Column'])

df = filter(df, 'Boolean Value')
df = rbind(df1, df2)

output = sqldf("SELECT * FROM df")



