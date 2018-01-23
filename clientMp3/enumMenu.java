
import java.lang.*;

public enum enumMenu {
    // pas utilisé pour le moment
    //Objets directement construits
    ADD(1, "ADD"),
    SEARCH(2, "SEARCH"),
    DEL(3, "DEL"),
    DISPLAY(4, "DISPLAY"),
    QUIT(5,"QUIT"),
    DOWNLOAD(6,"DOWNLOAD");

    private int id = 0;
    private String code = "";

    //Constructeur
    enumMenu(int id, String code){
        this.id = id;
        this.code = code;
    }

    public String getCode(){
        return code;
    }

    public int getId(){
        return id;
    }

    public String toString(){
        return getId() + " - " + getCode();
    }

    public static String getIdToCode(int idCode){
        for(enumMenu row : enumMenu.values()){
            if(row.getId() == idCode) {
                return row.getCode();
            }
        }
        return null;
    }

    public static enumMenu getIdToEnum(int idCode){
        for(enumMenu row : enumMenu.values()){
            if(row.getId() == idCode) {
                return row;
            }
        }
        return null;
    }
}