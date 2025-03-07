package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data element in the handle API for the PID status information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class STATUS extends HandleRecord {

  private int index;
  private HdlDataStatus data;

}
