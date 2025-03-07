package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data element in the handle API for the PID metadata license.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LICENSE extends HandleRecord {

  private int index;
  private HdlDataLicense data;

}
