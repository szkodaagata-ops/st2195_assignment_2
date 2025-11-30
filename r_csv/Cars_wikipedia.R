library(rvest)
wikipedia_url <- "https://en.wikipedia.org/w/index.php?title=Comma-separated_values&diff=prev&oldid=1075295751"
html <- read_html(wikipedia_url)
find_pre <- html_nodes(html, "pre")
all_texts <- html_text(find_pre)
cars <- all_texts[11]
cars_data_frame <- read.csv( text = cars, header = TRUE)
write.csv(cars_data_frame,"/Users/agataszkoda/Documents/Studia Data Science and Business Analytics LSE/Programming for Data Science/st2195_assignment_2/r_csv/cars.csv",row.names = FALSE)
