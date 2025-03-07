package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data element in the handle API for the resource info.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RESOURCE extends HandleRecord {

  private int index;
  private HdlDataResourceInfo data;

}
