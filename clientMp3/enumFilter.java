public enum enumFilter {
    //Objets directement construits
    TITLE(1, "name"),
    GENRE(2, "genre"),
    AUTHOR(3, "author"),
    URL(4, "url");

    private int id = 0;
    private String critere = "";

    //Constructeur
    enumFilter(int id, String critere){
        this.id = id;
        this.critere = critere;
    }

    public String getCritere(){
        return critere;
    }

    public int getId(){
        return id;
    }

    public String toString(){
        return getId() + " - " + getCritere();
    }

    public static String getIdToCritere(int idCritere){
        for(enumFilter row : enumFilter.values()){
            if(row.getId() == idCritere) {
                return row.getCritere();
            }
        }
        return null;
    }
}