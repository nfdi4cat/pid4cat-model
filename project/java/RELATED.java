package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data element in the handle API for related identifiers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RELATED extends HandleRecord {

  private int index;
  private HdlDataRelated data;

}
