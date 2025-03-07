package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data element in the handle API for the contact email.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EMAIL extends HandleRecord {

  private int index;
  private HdlDataContact data;

}
