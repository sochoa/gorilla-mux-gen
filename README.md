```
gorilla-mux-gen person    \
    first:string          \
    last:string           \
    middle:string         \
    suffix:string         \
    dateOfBirth:time.Time \
    gender:string         \
    aptNumber:int         \
    city:string           \
    zip:uint              \
    phone:int             \
    email:string          \
  | gofmt
```

Results in

```
import (
	"encoding/json"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	"strconv"
	"time"
)

type Person struct {
	PersonId    int64
	First       string    `json:first`
	Last        string    `json:last`
	Middle      string    `json:middle`
	Suffix      string    `json:suffix`
	DateOfBirth time.Time `json:dateOfBirth`
	Gender      string    `json:gender`
	AptNumber   int       `json:aptNumber`
	City        string    `json:city`
	Zip         uint      `json:zip`
	Phone       int       `json:phone`
	Email       string    `json:email`
}

var People []person

func createPerson(responseWriter http.ResponseWriter, request *http.Request) {
...
}

func getPeople(responseWriter http.ResponseWriter, request *http.Request) {
...
}

func getPerson(responseWriter http.ResponseWriter, request *http.Request) {
...
}

func updatePerson(responseWriter http.ResponseWriter, request *http.Request) {
...
}

func deletePerson(responseWriter http.ResponseWriter, request *http.Request) {
...
}

func AddRoutes(pathBase string, router *mux.Router) {
	router.HandleFunc(pathBase+"/people", createPerson).Methods("POST")
	router.HandleFunc(pathBase+"/people/{personId}", getPerson).Methods("GET")
	router.HandleFunc(pathBase+"/people", getPeople).Methods("GET")
	router.HandleFunc(pathBase+"/people/{personId}", updatePerson).Methods("PUT")
	router.HandleFunc(pathBase+"/people/{personId}", deletePerson).Methods("DELETE")
}

```
