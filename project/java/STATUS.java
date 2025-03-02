package None;

import java.util.List;
import lombok.*;






/**
  A data element in the handle API.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class STATUS extends HandleRecord {

  private Integer index;
  private HdlDataStatus data;

}
