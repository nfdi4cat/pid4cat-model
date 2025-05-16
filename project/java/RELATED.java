package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  The data element in the handle API for related identifiers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RELATED extends HandleRecord {

  private int index;
  private HdlDataRelated data;

}
