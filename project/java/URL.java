package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data element in the handle API for the landing page URL.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class URL extends HandleRecord {

  private int index;
  private HdlDataUrl data;

}
